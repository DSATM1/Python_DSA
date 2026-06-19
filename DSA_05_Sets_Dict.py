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

