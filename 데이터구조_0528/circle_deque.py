class CircularDeque(CircularQueue):
    def __init__(self, max_size):
        super().__init__(max_size)

    def add_rear(self, item):
        self.enqueue(item) # 원형 큐의 삽입과 동일

    def delete_front(self):
        return self.dequeue() # 원형 큐의 삭제와 동일

    def add_front(self, item):
        if self.is_full():
            print("덱이 가득 찼습니다.")
            return
        self.items[self.front] = item
        self.front = (self.front - 1 + self.max_size) % self.max_size

    def delete_rear(self):
        if self.is_empty():
            print("덱이 비어 있습니다.")
            return None
        item = self.items[self.rear]
        self.rear = (self.rear - 1 + self.max_size) % self.max_size
        return item