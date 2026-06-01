class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

def evaluate_postfix(expression):
    stack = Stack()

    for token in expression.split():
        if token.isdigit():
            stack.push(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            else:
                raise ValueError(f"Unknown operator: {token}")

            stack.push(result)

    if stack.size() != 1:
        raise ValueError("Invalid postfix expression")

    return stack.pop()

if __name__ == "__main__":
    print("후위 표기법 계산기입니다.")
    while True:
        try:
            expression = input("후위 표기법 수식을 입력하세요 (종료하려면 'exit' 입력): ")
            if expression.lower() == 'exit':
                print("계산기를 종료합니다.")
                break
            result = evaluate_postfix(expression)
            print(f"결과: {result}")
        except Exception as e:
            print(f"오류: {e}")