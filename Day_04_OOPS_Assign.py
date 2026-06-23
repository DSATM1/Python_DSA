"""key = ['a','b','c']
value = [1,2,3]
mu_dict = {k:v for k,v in zip(key,value)} 
print(mu_dict)"""



"""def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n //10
    return total

n = int(input("Enter N:").strip())
step = 1
while n>=10:
    n = sum_of_digits(n)
    step += 1

print(f"Digital Root : {n}")"""

"""class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def display(self):
        print(f"{self.brand} costs {self.price}")

m1 = Mobile("moto",10000)
m2 = Mobile("Vivo",14500)

m1.display()
m2.display()"""
