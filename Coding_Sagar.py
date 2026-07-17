"""for i in range(1,6):
    print("Step",i)"""

"""total = 0
for i in range(1,6):
    total += i
print(total)"""

"""i = 0
while i <= 5:
    print(i)
    i+=1"""

##---Even
"""i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1"""

##---Oddd
"""i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1"""


##---Reverse
"""i = 10
while i >= 1:
    print(i)
    i -= 1"""

"""i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1
print("Hi")"""

"""num = [1,2,3,4,5]
for i in num:
    if i == 3:
        continue
    print(i)"""

"""n = [1,2,3,4,5]
for j in n :
    if j == 2:
        pass
    else:
        print(j)"""

"""while True:
    user = input("Enter Number")
    if user == "S":
        break
    elif user.isdigit():
        print("Valid Number")
    else:
        pass"""

### ----- Strings ----- ###
"""d = 10
d1 = "10"
print(d + int(d1))"""

"""word = "   Suraj is a Fresh Candidate   "
print("Index Position of 3 :", word[3])
print("Total Char : ",len(word))
print(word.split())
print(word.replace("Suraj","Shree"))
print(word[-1])
print(word[0:20:3])
print(word.lower())
print(word.upper())
print(word[9:-3])
print(word[::-1])
print(word.strip())
print(word.lstrip())
print(word.rstrip())
print(word.startswith("   Suraj"))
print(word.endswith("Candidate   "))"""


"""user = input("Enter YES to Confirm:")
if user.upper() == "YES":
    print("Confirmed")
else:
    print("Retry")"""

"""lst = [23,43,67,89,9,12]
total = 0
for i in lst:
    total += i
print(total)"""

## --- This will print only the target but we need index position  
"""lst = [1,2,3,4,5]
target = 3
result = []
for i in lst:
    if i == target:
        result.append(i)
print(result)"""

## --- Now using for while loop 

"""lst = [23,34,45,5,6]
target = 5

index = -1
i = 0

while i < len(lst):
    if lst[i] == target:
        index = i
        break
    i += 1
print(index)"""