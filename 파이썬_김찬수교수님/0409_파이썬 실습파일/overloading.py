class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1)
print(str(p1))
print(format(p1))
# print(p1 + p2)