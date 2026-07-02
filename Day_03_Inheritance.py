#-----Inhertance and Polymorphism-------

"""class user:
    def __init__(self,uname):
        self.uname=uname
        #self.__pwd = pwd

    def login(self):
        print(f"{self.uname} logged in ")

    
class Admin(user):
    def delete_user(self):
        print("Admin deleted user")

a = Admin("Suraj")
print(a.uname)
a.delete_user()
a.login()"""


"""class Family:
    def __init__(self,sur_name):
        self.sur_name=sur_name
    
class Child(Family):
    def __init__(self,sur_name,name):
        super().__init__(sur_name)
        self.name=name

child = Child ("Pokale","Suraj")
print(f"{child.name} {child.sur_name}")"""


"""class Animal:
    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

ani = [Dog(),Cat()]
for a in ani:
    a.make_sound()"""


#----Getters and Setters------

"""class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

s = Student("Suraj",24)

print(s.get_name())

s.set_name("SP")

print(s.get_name())"""


"""from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Bike(Vehicle):
    def __init__(self, name):
        self.name = name

    def start_engine(self):
        print("Engine Started")

b = Bike("Royal Enfield")

print(b.name)

b.start_engine()"""