class Parrot:
    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:
    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")

def flying_test(bird): # 공통 인터페이스
    bird.fly()

def swiming_test(h):
    h.swim()

blu = Parrot()
peggy = Penguin()

flying_test(blu)
flying_test(peggy)

swiming_test(blu)
swiming_test(peggy)