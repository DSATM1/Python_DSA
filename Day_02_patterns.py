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