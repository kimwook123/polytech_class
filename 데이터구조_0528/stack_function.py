class StackADT:
    def __init__(self, capacity=100):
        self.items = []
        self.capacity = capacity

    def push(self, e):
        if not self.isFull():
            self.items.append(e)
        else:
            print("Stack Overflow: 스택이 가득 찼습니다.")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack Underflow: 스택이 비어 있습니다.")
            return None

    def isFull(self):
        return len(self.items) >= self.capacity

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def display(self):
        print("Stack (top -> bottom):", self.items[::-1])

if __name__ == "__main__":
    s = StackADT(5)

    s.push('A')
    s.push('B')
    s.push('C')

    print(f"현재 상단 항목(Peek): {s.peek()}")
    print(f"스택 크기: {s.size()}")

    print(f"꺼낸 항목(Pop): {s.pop()}")
    print(f"꺼낸 항목(Pop): {s.pop()}")

    s.display()

    s.clear()
    print(f"비어 있나요? {s.isEmpty()}")