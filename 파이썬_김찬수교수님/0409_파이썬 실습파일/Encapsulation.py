class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"Selling Price : {self.__maxprice}")
    
    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000 # 임의로 못바꿈
c.sell()

# 클래스 내 메소드 중 인자값을 바꿀 수 있는 메소드 호출
c.setMaxPrice(1000)
c.sell()