class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = [None] * max_size
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def enqueue(self, item):
        if self.is_full():
            print("큐가 가득 찼습니다.")
            return
        self.rear = (self.rear + 1) % self.max_size
        self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("큐가 비어 있습니다.")
            return None
        self.front = (self.front + 1) % self.max_size
        return self.items[self.front]

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        elif self.front > self.rear:
            out = self.items[self.front+1:self.max_size] + self.items[0:self.rear+1]
        print("원형 큐:", out)