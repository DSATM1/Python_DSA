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



# two_sum([2,7,11,15], 9)  → [0, 1]
# two_sum([3,2,4], 6)      → [1, 2]
# two_sum([1,2,3], 10)     → None

"""def two_sum(nums,target):
    n = len(nums)
    dct = {}
    for i in range(n):
        rem = target - nums[i]
        if rem in dct:
            return [dct[rem],i]
        dct[nums[i]] = i
print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
print(two_sum([1,2,3], 10))"""



# {"a":1, "b":2}  →  {1:"a", 2:"b"}
# for dept,name in result.items():
#      print(f"{dept} : {name}")

"""def inverted_dct(dct):
    inverted = {}
    for key,value in dct.items():
        inverted [value] =key
    return inverted
print(inverted_dct({"a":1,"b":2}))"""


# Anagram Checker
# "listen" → frequency dict → {'l':1, 'i':1, 's':1, 't':1, 'e':1, 'n':1}
# "silent" → frequency dict → {'s':1, 'i':1, 'l':1, 'e':1, 'n':1, 't':1}

#-----Approach 1-------
"""def is_anagram(s,t):
    if len(s) != len(t):
        return False 
    freq = {}
    for i in s:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    
    for i in t:
        if i not in freq:
            return False
        else:
            freq[i] -= 1

    for i in freq.values():
        if i != 0:
            return False
    return True 

print(is_anagram("listen","silent"))"""

#-----Approach 2-----------
"""def is_anagram(s, t):
    s = s.lower().replace(" ", "")
    t = t.lower().replace(" ", "")
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in t:
        freq[ch] = freq.get(ch, 0) - 1
    return all(v == 0 for v in freq.values())

print(is_anagram("listen","silent"))"""

#---------Approach 3-------------
"""def is_anagram(s, t):
    s = s.lower().replace(" ", "")
    t = t.lower().replace(" ", "")
    return sorted(s) == sorted(t)   # one line!
print(is_anagram("listen","silent"))"""



# Build a nested dict for 3 students with subject marks. 
# Write functions to get total, average, grade. Print full report!
# ===== Report Card =====
# Suraj | Total: 440 | Avg: 88.00 | Grade: A
# Putta | Total: 395 | Avg: 79.00 | Grade: B
# Ravi  | Total: 460 | Avg: 92.00 | Grade: A+

"""def get_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80: 
        return "A"
    elif avg >= 70: 
        return "B"
    elif avg >= 60: 
        return "C"
    else:       
        return "F"
def print_report(students):
    for name,subjects in students.items():
        total = sum(subjects.values())
        avg = total/len(subjects)
        grade = get_grade(avg)
        print(f"{name} | Total: {total} | Avg: {avg:.2f} | Grade: {grade}")

print_report(students = {
    "Suraj": {"python": 90, "dsa": 88, "sql": 92, "ml": 85, "os": 85},
    "Putta": {"python": 78, "dsa": 80, "sql": 75, "ml": 82, "os": 80},
    "Ravi" : {"python": 95, "dsa": 92, "sql": 90, "ml": 88, "os": 95}
}  )"""




# Top K Frequent Elements (LeetCode #347!)
# Given a list of numbers, find the K most frequently appearing elements. 
# Return in order of frequency!
# top_k([1,1,1,2,2,3], k=2)       → [1, 2]
# top_k([1,2,3,4,5,5,5,4,4], k=2) → [5, 4]
"""def topKFrequent(nums, k):
    count = {}
    for i in nums:
        count[i] = count.get(i,0)+1
    sot = sorted(count, key=lambda x: count[x], reverse=True)
    return sot[:k]
print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1,2,3,4,5,5,5,4,4], 2))"""

