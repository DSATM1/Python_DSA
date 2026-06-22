"""coordinates = (10, 20,30) # 2D point 
rgb = (255, 0, 128) # RGB color 
mixed = (1, "hello", 3.14, True) # mixed types 
single = (42,) # single item needs comma! 
empty = () # empty tuple 
print(len(coordinates)) # 2 
print(type(coordinates)) # <class 'tuple'>
print(rgb)
print(mixed)
print(single)
print(empty)"""


"""point = (10, 20) 
print(point[0]) # 10 — index like lists 
print(point[-1]) # 20 — negative index works 
x, y = point # unpack: 
x=10 
y=20 
print(f"Point: {x}, {y}") 
a, b, c = (1, 2, 3) # unpack 3 values at once 
print(a, b, c) # 1 2 3"""

"""nums = (1, 2, 2, 3, 2, 4) 
print(nums.count(2)) # 3 — count occurrences 
print(nums.index(3)) # 3 — index of first 3 
print(sum(nums)) # 12 — built-in sum() 
print(max(nums)) # 4 — built-in max() # Cannot modify! 
nums[0] = 2 # ❌ TypeError!"""

###### ----- Sets ------- #######

"""colors = {"red", "green", "blue"} # set with items 
unique = set([1, 2, 2, 3, 3, 3]) # removes duplicates → {1, 2, 3} 
empty = set() # empty set (NOT {}) 
print(len(colors)) # 3 
print(type(colors)) # <class 'set'> 
print(unique) # {1, 2, 3}"""


"""colors = {"red", "green", "blue"} # Add & Remove 
colors.add("yellow") # {red, green, blue, yellow} 
colors.remove("red") # {green, blue, yellow} 
colors.discard("purple") # no error if item missing 
colors.pop() # remove any item # Checking membership (super fast!) 
print("green" in colors) # True ← O(1) speed! 
print("red" in colors) # False # Set math operations 
a = {1, 2, 3, 4} 
b = {3, 4, 5, 6} 
print(a | b) # {1, 2, 3, 4, 5, 6} — union (OR) 
print(a & b) # {3, 4} — intersection (AND) 
print(a - b) # {1, 2} — difference 
print(a ^ b) # {1, 2, 5, 6} — symmetric difference"""



###### ----Dictionaries----- #######


"""student = { 
    "name": "Suraj", 
    "age": 23, 
    "cgpa": 8.52, 
    "college": "DSATM" 
    } 
empty = {} 
from_list = dict([("a", 1), ("b", 2)]) # from list of pairs 
print(len(student)) # 4 
print(type(student)) # <class 'dict'>"""



"""student = {"name": "Suraj", "age": 23, "cgpa": 8.52} # Using keys 
print(student["name"]) # Suraj 
print(student["age"]) # 23 
print(student["cgpa"]) # ❌ KeyError! # Safe access with .get() 
print(student.get("name")) # Suraj 
print(student.get("city")) # None (no error!) 
print(student.get("city", "Unknown")) # Unknown (default value)"""


"""student = {"name": "Suraj", "age": 23} # Add new key-value 
student["city"] = "Bengaluru" 
student["cgpa"] = 8.52 # Update existing 
student["age"] = 24 # Remove del 
student["city"] # delete by key 
print(student) # {"name": "Suraj", "cgpa": 8.52}
student.pop("age") # remove & return value 
student.clear() # remove all """



"""student = {"name": "Suraj", "age": 23, "cgpa": 8.52} # Keys only 
for key in student: 
    print(key) # name, age, cgpa # Keys and values 
for key, value in student.items(): 
    print(f"{key} = {value}") # name = Suraj, etc. # Values only 
for value in student.values(): 
    print(value) # Suraj, 23, 8.52 # Check if key exists 
if "name" in student: 
    print("Name found!")"""



"""school = { 
    "students": [ 
        {"name": "Suraj", "marks": 85}, 
        {"name": "Putta", "marks": 92} 
    ], 
        "location": "Bengaluru", 
        "courses": { "python": 30, 
                    "dsa": 45, 
                    "databases": 25 
                    }
} # Access nested data 
print(school["location"]) # Bengaluru 
print(school["students"][0]["name"]) # Suraj 
print(school["courses"]["python"]) # 30"""

"""student = {"name": "Suraj", "age": 23}
print(student.get("cgpa"))"""