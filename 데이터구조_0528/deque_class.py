class LinearDeque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def delete_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def delete_rear(self):
        if not self.is_empty():
            return self.items.pop()
        return None