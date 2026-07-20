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



## --- List
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



"""## --- Now using for For loop 
lst = [1,2,3,4,5]
target = 7
count  = 0 
index = "Not Found" # if user enters num which is not in the list 

for i in lst:
    if i == target:
        index = count
        break
    count += 1
print(index)"""


"""lst = [10, 20, 30, 49, 56]
target = int(input("Enter target number: "))
found = False
position = -1

for i in range(len(lst)):
    if lst[i] == target:
        found = True
        position = i
        break

if found:
    print("Found at position", position)
elif target < lst[0] or target > lst[-1]:
    print("Out of range")
else:
    print("Not found")"""




"""my_list = [21,39,43,56,61,78,92,18,43,89,75,10,83,43,32]
my_list.append(23)
my_list.extend([2,1,3])
# my_list.append("Yes")
# my_list.extend("Suraj")
# my_list.insert(3,"Shree")
# my_list.remove("Yes")
#my_list.sort(reverse=True)
z = my_list.count(43)
# z = my_list.pop()
print(len(my_list))
print(my_list)
print(z)
# print(z+100)"""

"""lst = [10,20,30,40]
l2 = lst.pop()
print(lst)
print(l2+100)"""


## -- Shallow Copy and DeepCopy
"""import copy
a =[1,2,[3,4]]
v = copy.deepcopy(a)
v[2].append(8)
print(f"A = ",a)
print(f"V = ",v)"""


### --- Tuple --- ###
"""days = ("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
print(days)

for day in days:
    print(day)
print(days.count("Sun"))
print(days.index("Fri"))
print(len(days))"""

### --- Set --- ###

"""s = {"name","Address","PH No","Age"}
print(type(s))
print(s)
# print(s[0]) not ordered"""

"""s = {2,4,6,8,7}
p = {1,3,5,7}
print(s | p) # union = all from both sets
print(s & p) # intersection = only elements in both set like 7 
print(s - p) # extra s - p only s will consider with unique not in both set like 7 it's in both ok """


"""s = {1,2,3,4,5,6}
s.add(9)
print(s)
s.remove(2)
print(s)
s.discard(5)
print(s)"""

"""fs = frozenset([1,2,1,3,4,2,1,2,3])
#fs.add(9)
#fs.remove(3)
#fs.discard(4)
# u can't do any operations in frozenset
print(fs)"""

##--Dictionary--##
Student = {
    "name":"Suraj",
    "Age":24,
    "Address":"AGS Layout"
}
#print(Student)


#Student.pop("Age")
#print(Student)

print(Student.keys())

print(Student["Age"])
print(Student["name"])
print(Student["Address"])




