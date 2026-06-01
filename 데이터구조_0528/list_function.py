class CustomList:
    def __init__(self, capacity=100):
        self.items = []
        self.capacity = capacity

    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= len(self.items):
            self.items.insert(pos, e)
        else:
            print("오류: 삽입 범위를 벗어났거나 리스트가 가득 찼습니다.")

    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < len(self.items):
            return self.items.pop(pos)
        else:
            print("오류: 삭제할 수 없는 위치입니다.")
            return None

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) >= self.capacity

    def getEntry(self, pos):
        if 0 <= pos < len(self.items):
            return self.items[pos]
        return None

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def find(self, item):
        try:
            return self.items.index(item)
        except ValueError:
            return -1

    def replace(self, pos, item):
        if 0 <= pos < len(self.items):
            self.items[pos] = item
        else:
            print("오류: 잘못된 위치입니다.")

    def sort(self):
        self.items.sort()

    def merge(self, other_list):
        if isinstance(other_list, CustomList):
            self.items.extend(other_list.items)
        else:
            self.items.extend(other_list)

    def display(self):
        print(f"List (Size: {self.size()}): {self.items}")

    def append(self, e):
        if not self.isFull():
            self.items.append(e)
        else:
            print("오류: 리스트가 가득 찼습니다.")

if __name__ == "__main__":
    mylist = CustomList(capacity=10)

    mylist.append(10)
    mylist.append(30)
    mylist.insert(1, 20)
    mylist.display()

    print("삭제된 요소:", mylist.delete(0))
    mylist.replace(1, 50)
    mylist.display()

    print("20의 위치:", mylist.find(20))
    print("현재 크기:", mylist.size())

    mylist.merge([100, 5, 80])
    mylist.sort()
    mylist.display()

    mylist.clear()
    print("비어있나요?", mylist.isEmpty())