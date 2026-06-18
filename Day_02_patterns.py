#--------Patterns-------


"""n = 5
for i in range(1,n+1):
    for j in range(i,n+1):
        print("*",end= " ")
    print()"""


"""n = 5
for i in range(0,n):
    for j in range(0, i+1):
        print("*",end= " ")
    print()"""

"""n = 5

for i in range(1, n+1):
    spaces = n - i
    stars = i
    print(" " * +spaces +"* " *+stars)

for i in range(1 , n):
    spaces = i
    stars = n - i 
    print(" " * +spaces +"* " *+stars)"""



"""n = 4
counter = 1
for i in range(0,n+1):
    for j in range(0,i):
        print(counter, end = " ")
        counter += 1
    print()"""



"""def positive(lst):
    result = []
    for i in lst:
        if i > 0:
            result.append(i)
    return result      
l = [-1,2,0,3,-2,-5,4,3,0]
print(positive(l))

# l = [-1,2,0,3,-2,-5,4,3,0]
# Now i need only +ve num from l """

"""n = 6
if n <= 0:
    print("Print only +ve numbers")
else:
    step = 0
    while n != 1:
        print(n,end = "->")
        if n % 2 == 0 :
            n = n//2
        else:
            n = n * 3 + 1
        step += 1
    print(n)
    print(f"Steps = {step}")"""