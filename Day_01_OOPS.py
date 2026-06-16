#----------OOP'S-----------

"""class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} is walking and the Age is {self.age}")
peeru = Human("Suraj",24)
peeru.walk()

saaru = Human("Shree",19)
saaru.walk()"""


"""class Person:
    def __init__(self,Boy,Girl):
        self.Bname=Boy
        self.Gname=Girl
    def intro(self):
        print(f"Kunal is a {self.Bname} and Mahita is {self.Gname}")
gender = Person("Male","Female")
gender.Gname="Shree"  #changing the argument
gender.intro()"""

"""class ATM:
    def __init__(self,balance):
        self.balance = balance
    def check_bal(self):
        print(self.balance)
sp = ATM(23000)
###sp.balance = 20000  this is not private so use private attribute like "__" ex = __balance
print(sp.balance)"""

"""class Database:
    def __init__(self):
        self.__storage = {}

    def save_data(self, key, value):
        self.__storage[key] = value
        print(f"Data saved for {key}")
    
    def get_data(self, key):
        return self.__storage.get(key, "no data found")

db = Database()
db.save_data("us_01", {"name":"Raj","age":30})
print(db.get_data("us_01"))"""