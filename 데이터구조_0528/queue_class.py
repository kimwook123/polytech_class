class LinearQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0) # 첫 번째 요소 제거 및 반환
        return None

    def display(self):
        print("선형 큐:", self.items)