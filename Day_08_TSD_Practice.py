#---Tuple----Sets-----Dict-----Practices----Questions

# Output:
# Marks : (85, 92, 78, 95, 88)
# Min   : 78  |  Max : 95
# Sum   : 438  |  Avg : 87.60
# 85 in marks : True

"""marks = (85, 92, 78, 95, 88)
Min = min((85, 92, 78, 95, 88))
Max = max((85, 92, 78, 95, 88))
Sum = sum((85, 92, 78, 95, 88))
Avg = (Sum/len(marks))
c = 85 in marks
print(f"Marks : {marks}")
print(f"Min   : {Min}  | Max : {Max}")
print(f"Sum   : {Sum} | Avg : {Avg:.2f}")
print(f"85 in Marks : {c}")"""

# Both courses     : {"Ravi", "Kiran"}
# Only Python      : {"Suraj", "Putta"}
# Total applicants : 6 unique students

# a = {1, 2, 3, 4} 
# b = {3, 4, 5, 6} 
# print(a | b) # {1, 2, 3, 4, 5, 6} — union (OR) 
# print(a & b) # {3, 4} — intersection (AND) 
# print(a - b) # {1, 2} — difference 
# print(a ^ b) # {1, 2, 5, 6} — symmetric difference


"""python_applicants = {"Suraj","Putta","Ravi","Kiran"}
dsa_applicants = {"Ravi","Kiran","Meena","Arjun"}
print(f"Both courses     : {python_applicants & dsa_applicants}")
print(f"Only Python      : {python_applicants - dsa_applicants}")
print(f"Total applicants : {len(python_applicants | dsa_applicants)} unique students")"""

"""phone_book = {
    "Suraj"   :1,
    "Mohan"   :2,
    "Muruli"  :3,
    "Prajwal" :4,
    "Likith"  :5
    }

name = input("enter the name").strip()
result = phone_book.get(name)
if result:
    print(result)
else:
    print("Contact Not Found")"""