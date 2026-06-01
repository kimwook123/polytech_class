import tkinter as tk


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if not self.items:
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class CalculatorEngine:
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '%': 2,
        '^': 3,
    }

    @staticmethod
    def tokenize(expr):
        tokens = []
        number = ''
        for ch in expr:
            if ch.isdigit() or ch == '.':
                number += ch
            else:
                if number:
                    tokens.append(number)
                    number = ''
                if ch.strip():
                    tokens.append(ch)
        if number:
            tokens.append(number)
        return tokens

    @staticmethod
    def infix_to_postfix(tokens):
        output = []
        ops = Stack()

        for token in tokens:
            if token.replace('.', '', 1).isdigit():
                output.append(token)
            elif token == '(':
                ops.push(token)
            elif token == ')':
                while not ops.is_empty() and ops.peek() != '(':
                    output.append(ops.pop())
                if ops.is_empty():
                    raise ValueError("Mismatched parentheses")
                ops.pop()
            else:
                while not ops.is_empty() and ops.peek() in CalculatorEngine.precedence and \
                        CalculatorEngine.precedence[ops.peek()] >= CalculatorEngine.precedence[token]:
                    output.append(ops.pop())
                ops.push(token)

        while not ops.is_empty():
            op = ops.pop()
            if op in ('(', ')'):
                raise ValueError("Mismatched parentheses")
            output.append(op)

        return output

    @staticmethod
    def evaluate_postfix(postfix):
        values = Stack()

        for token in postfix:
            if token.replace('.', '', 1).isdigit():
                values.push(float(token))
            else:
                if values.size() < 2:
                    raise ValueError("Invalid expression")
                b = values.pop()
                a = values.pop()

                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    if b == 0:
                        raise ZeroDivisionError("Division by zero")
                    result = a / b
                elif token == '%':
                    result = a % b
                elif token == '^':
                    result = a ** b
                else:
                    raise ValueError(f"Unknown operator: {token}")

                values.push(result)

        if values.size() != 1:
            raise ValueError("Invalid expression")

        return values.pop()

    @classmethod
    def evaluate(cls, expr):
        tokens = cls.tokenize(expr)
        postfix = cls.infix_to_postfix(tokens)
        result = cls.evaluate_postfix(postfix)
        return result


class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python 계산기")
        self.geometry("360x500")
        self.resizable(False, False)

        self.expression = tk.StringVar(value="")
        self.result = tk.StringVar(value="0")

        self._build_ui()

    def _build_ui(self):
        display_frame = tk.Frame(self, bg="#1E1E1E", padx=16, pady=16)
        display_frame.pack(fill="x", padx=10, pady=10)

        expression_label = tk.Label(
            display_frame,
            textvariable=self.expression,
            anchor="e",
            justify="right",
            bg="#1E1E1E",
            fg="#B0B0B0",
            font=("Segoe UI", 18),
        )
        expression_label.pack(fill="x")

        result_label = tk.Label(
            display_frame,
            textvariable=self.result,
            anchor="e",
            justify="right",
            bg="#1E1E1E",
            fg="white",
            font=("Segoe UI", 36, "bold"),
        )
        result_label.pack(fill="x", pady=(10, 0))

        button_frame = tk.Frame(self, bg="#121212")
        button_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        buttons = [
            ["C", "⌫", "(", ")"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "^", "+"],
            ["=",],
        ]

        for row, row_buttons in enumerate(buttons):
            for col, label in enumerate(row_buttons):
                btn = tk.Button(
                    button_frame,
                    text=label,
                    font=("Segoe UI", 18, "bold"),
                    width=6,
                    height=2,
                    bg="#2B2B2B" if label not in {"=", "+", "-", "*", "/", "^"} else "#3A3A3A",
                    fg="white",
                    relief="flat",
                    command=lambda value=label: self.on_button(value),
                )
                btn.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

        for i in range(5):
            button_frame.grid_columnconfigure(i, weight=1)
        for i in range(len(buttons)):
            button_frame.grid_rowconfigure(i, weight=1)

    def on_button(self, value):
        current = self.expression.get()

        if value == "C":
            self.expression.set("")
            self.result.set("0")
            return

        if value == "⌫":
            if current:
                self.expression.set(current[:-1])
            return

        if value == "=":
            try:
                evaluated = CalculatorEngine.evaluate(current)
                self.result.set(self._format_result(evaluated))
            except Exception as e:
                self.expression.set("Error")
                self.result.set("0")
            return

        if current == "Error":
            current = ""

        self.expression.set(current + value)

    @staticmethod
    def _format_result(value):
        if float(value).is_integer():
            return str(int(value))
        return str(value)


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
