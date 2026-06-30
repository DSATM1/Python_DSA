
# Given a list of integers, find and print all duplicate numbers. 
# A duplicate is any number that appears more than once. 
# Print each duplicate only once, in the order they first repeated.

# Input:  [1, 3, 4, 2, 2, 3, 5, 4, 4]
# Output: Duplicates: [2, 3, 4]

"""def duplicates(unique):
    result = []
    for i in unique:
        if unique.count(i) > 1 and i not in  result :
            result.append(i)
        
    return result

unique = duplicates([1, 3, 4, 2, 2, 3, 5, 4, 4])
print(sorted(unique))"""


# Write a function word_frequency(sentence) that takes a sentence string and returns a dictionary 
# with each word as the key and its frequency as the value.

# Input:  "the cat sat on the mat the cat"
# Output: {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}

"""def count_word(sent):                              #type:ignore
    count = {}
    for word in sent.split():                         #type:ignore
        count[word] = count.get(word,0)+1             #type:ignore
    return count                                      #type:ignore
print(count_word("the cat sat on the mat the cat"))   #type:ignore"""


# Write a function are_anagrams(s1, s2) that returns True if two 
# strings are anagrams of each other. Ignore case and spaces.

# "listen",     "silent"      → True
# "hello",      "world"       → False
# "Astronomer", "Moon starer" → True

"""def is_anagram(s, t):
    s = s.lower().replace(" ", "")
    t = t.lower().replace(" ", "")
    return sorted(s) == sorted(t)   # one line!
print(is_anagram("listen","silent"))"""


"""def is_palindrome(s):
    s = s.strip()
    s = s.lower()
    s = s.replace(" ","")
    return s == s[::-1]

print(is_palindrome("racecar"))                     # True
print(is_palindrome("hello"))                       # False
print(is_palindrome("A man a plan a canal Panama")) # True"""

"""def two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return (left + 1, right + 1)   # 1-based indexing

        elif current_sum < target:
            left += 1

        else:
            right -= 1
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([2, 3, 4], 6))
print(two_sum([1, 4, 6, 9], 10))"""


grades = {
    "Suraj": {"Maths": 88, "Science": 92, "English": 79},
    "Arjun": {"Maths": 76, "Science": 85, "English": 90},
    "Priya": {"Maths": 95, "Science": 88, "English": 84},
}

# Function 1: Calculate average marks of a student
def get_average(name, grades):
    marks = grades[name].values()
    average = sum(marks) / len(marks)
    return round(average, 2)


# Function 2: Find the class topper
def class_topper(grades):
    topper = ""
    highest_average = 0

    for student in grades:
        avg = get_average(student, grades)

        if avg > highest_average:
            highest_average = avg
            topper = student

    return topper


# Function 3: Find the topper in a subject
def subject_topper(subject, grades):
    topper = ""
    highest_marks = 0

    for student in grades:
        marks = grades[student][subject]

        if marks > highest_marks:
            highest_marks = marks
            topper = student

    return topper


# Testing
print("Average of Suraj:", get_average("Suraj", grades))
print("Class Topper:", class_topper(grades))
print("Maths Topper:", subject_topper("Maths", grades))
print("Science Topper:", subject_topper("Science", grades))
print("English Topper:", subject_topper("English", grades))