class CustomList:
    def __init__(self, capacity=100):
        self.items = []          # 내부 저장소 (리스트)
        self.capacity = capacity # 리스트의 최대 용량

    # 1. pos 위치에 요소 e 삽입
    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= len(self.items):
            self.items.insert(pos, e)
        else:
            print("오류: 삽입 범위를 벗어났거나 리스트가 가득 찼습니다.")

    # 2. pos 위치의 요소 삭제 및 반환
    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < len(self.items):
            return self.items.pop(pos)
        else:
            print("오류: 삭제할 수 없는 위치입니다.")
            return None

    # 3. 리스트가 비어 있는지 검사
    def isEmpty(self):
        return len(self.items) == 0

    # 4. 리스트가 가득 차 있는지 검사
    def isFull(self):
        return len(self.items) >= self.capacity

    # 5. pos 위치의 요소 반환
    def getEntry(self, pos):
        if 0 <= pos < len(self.items):
            return self.items[pos]
        return None

    # 6. 리스트 안의 요소 개수 반환
    def size(self):
        return len(self.items)

    # 7. 리스트 초기화
    def clear(self):
        self.items = []

    # 8. item이 있는 인덱스 반환
    def find(self, item):
        try:
            return self.items.index(item)
        except ValueError:
            return -1  # 항목이 없는 경우 -1 반환

    # 9. pos 위치의 항목을 item으로 교체
    def replace(self, pos, item):
        if 0 <= pos < len(self.items):
            self.items[pos] = item
        else:
            print("오류: 잘못된 위치입니다.")

    # 10. 리스트 정렬
    def sort(self):
        self.items.sort()

    # 11. 다른 리스트를 현재 리스트에 추가
    def merge(self, other_list):
        # other_list가 클래스 객체일 경우와 일반 파이썬 리스트일 경우 모두 대응
        if isinstance(other_list, CustomList):
            self.items.extend(other_list.items)
        else:
            self.items.extend(other_list)

    # 12. 리스트 화면 출력
    def display(self):
        print(f"List (Size: {self.size()}): {self.items}")

    # 13. 맨 뒤에 새로운 항목 추가
    def append(self, e):
        if not self.isFull():
            self.items.append(e)
        else:
            print("오류: 리스트가 가득 찼습니다.")

if __name__ == "__main__":
    # 리스트 생성 (최대 용량 10)
    mylist = CustomList(capacity=10)

    mylist.append(10)
    mylist.append(30)
    mylist.insert(1, 20)  # [10, 20, 30]
    mylist.display()

    print("삭제된 요소:", mylist.delete(0)) # 10 삭제
    mylist.replace(1, 50) # 인덱스 1의 30을 50으로 교체
    mylist.display()

    print("20의 위치:", mylist.find(20))
    print("현재 크기:", mylist.size())

    mylist.merge([100, 5, 80])
    mylist.sort()
    mylist.display()

    mylist.clear()
    print("비어있나요?", mylist.isEmpty())