class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} is walking and the Age is {self.age}")
peeru = Human("Suraj",24)
peeru.walk()

saaru = Human("Shree",19)
saaru.walk()