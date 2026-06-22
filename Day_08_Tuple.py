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