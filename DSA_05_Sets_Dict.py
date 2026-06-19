#-----Sets and Dictionaries-------

"""set1 = {2,3,4,5,"hello","Bye"}
print(set1)
print(type(set1))"""

"""#Empty Set
s = set()
print(type(s))"""



#Unique Elements convert from list to set 
"""list1 = [2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,0,0,1,1]
set1 = set(list1)
print(len(set1))
print(set1)"""

"""set1 = {"Suraj",23,"Age",100,"Lucifer"}
set1.add(100)
set1.add("SP")
set1.discard("Age")

set1.remove("SP")
print(set1)"""

"""set1 = {"Suraj",23,"Age",100,"Lucifer"}

if "Sura" in set1:
    print(True)
else:
    print(False)

set1.clear()
print(set1)"""



"""# Deep Copy full elements from both sets 
# shallow copy only present elements [Copy()]
set1 = {1,2,3}
set2 = set1.copy()

set2.add(4)

print(set1)
print(set2)"""


"""set1 = {1,8,7,2,4}
set2 = {8,2,9,6}

print(set1|set2)
print(set1.union(set2))"""

"""set1 = {1,8,7,2,4}
set2 = {8,2,9,6}

print(set1&set2)
print(set1.intersection(set2))"""


"""set1 = {1,8,7,2,4}
set2 = {8,2,9,6}

print(set1-set2)
print(set2-set1)
print(set1.difference(set2))
print(set2.difference(set1))"""



"""set1 = {1,8,7,2,4}
set2 = {8,2,9,6}
#union - intersection
print(set1^set2)
print(set1.symmetric_difference(set2))"""


"""dict1 = {
    1:"Name",
    "Hello":100,
    10.25:"Float",
    "Bool":True
}

print(dict1)
print(len(dict1))
print(type(dict1))"""


"""dct = {
    (1,2,3):"Tuple",
    "Name":"String"
}
print(dct["Name"])"""



"""dct1 = {
    1:"Suraj",
    2:"Manu",
    3:"Nags",
    4:"Sam"
}

dct1[5] = "Sam"  # Key should be unique not the value 

dct1.update({
    1:"SP",
    6:"Rohan"
})
print(dct1)"""

"""dct = dict(Suraj=7,Mohan = 23)
print(dct)"""


"""dct1 = {
    1:"Suraj",
    2:"Manu",
    3:"Nags",
    4:"Sam"
}

dct1.pop(4)
del dct1[1]
print(dct1)"""

"""dct1 = {
    1:"Suraj",
    2:"Manu",
    3:"Nags",
    4:"Sam"
}

print(dct1.items())
for key,value in dct1.items():
    print(key,value)

for key in dct1.keys():
    print(key,end=" ")

for key in dct1.items():
    print(key,end=" ")

for value in dct1.values():
    print(value,end=" ")"""