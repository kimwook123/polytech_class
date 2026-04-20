class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return f"{self.name} sings {song}"
    
    def dance(self):
        return f"{self.name} is now dancing"

kim = Human("kim", 10)

print(kim.sing("'Only Hope'"))
print(kim.dance())
