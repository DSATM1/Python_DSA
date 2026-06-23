#---Extra Practice----

# nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# Frequency : {1:1, 2:2, 3:3, 4:4}
# Duplicates: {2:2, 3:3, 4:4}

"""def count_num(lst):
    count = {}
    for l in lst:
        count[l] = count.get(l,0)+1
    dct = {}
    for key,value in count.items():
        if value > 1:
            dct[key] = value 
    
    return count, dct
freq,dup = count_num([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(f"Frequency  : {freq}")
print(f"Duplicates : {dup}")"""



# students = [("Suraj","MCA"),("Putta","BCA"),("Ravi","MCA"),("Kiran","BCA"),("Meena","MBA")]

# MCA : ["Suraj", "Ravi"]
# BCA : ["Putta", "Kiran"]
# MBA : ["Meena"]

"""def sort_dept(students):
        group = {}
        for name, dept in students:
            if dept not in group:
                group[dept] = []
            group[dept].append(name)
        return group
result = sort_dept([("Suraj","MCA"),("Putta","BCA"),
            ("Ravi","MCA"),("Kiran","BCA"),
            ("Meena","MBA")])

for dept,name in result.items():
     print(f"{dept} : {name}")
     
# print(f"MCA : {result["MCA"]}")
# print(f"BCA : {result["BCA"]}")
# print(f"MBA : {result["MBA"]}")"""