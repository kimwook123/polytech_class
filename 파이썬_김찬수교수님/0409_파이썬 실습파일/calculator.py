class calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def plus(self):
        return self.x + self.y 
    def minus(self):
        return self.x - self.y
    def multiple(self):
        return self.x * self.y
    def divide(self):
        try:
            dividing = self.x/self.y
            return dividing
        except ZeroDivisionError as e:
            print(f"발생한 에러: {e}")
            return 0
        
try:
    number1 = int(input("첫 번째 숫자를 입력하세요.\n"))
    number2 = int(input("두 번째 숫자를 입력하세요.\n"))
except ValueError:
    print("숫자만 입력해야 합니다!")

while True:
    how = input("+, -, *, /중에 하나 고르세요.\n")
    if how in ['+', '-', '*', '/']:
        break
    else:
        print("계산 기호를 올바르게 입력하세요.")

key = calculator(number1, number2)

if how == '+':
    print(f"결과: {key.plus()}")
elif how == '-':
    print(f"결과: {key.minus()}")
elif how == '*':
    print(f"결과: {key.multiple()}")
elif how == '/':
    print(f"결과: {key.divide()}")