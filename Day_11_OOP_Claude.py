# 🐯 Tiger Mode — Day 8
# New Concept: Object-Oriented Programming (OOP)

"""class Dog:
    def __init__(self, name):   # runs when object is created
        self.name = name        # self = this specific object

    def bark(self):
        print(self.name + " says: Woof!")

d = Dog("Bruno")   # create an object
d.bark()           # → Bruno says: Woof!"""

# A good approach is:

# Convert the string to lowercase.
# Ignore spaces.
# Count the frequency of each character using a dictionary.
# Find the character with the highest frequency.
# If two characters have the same frequency, return the one that appeared first.

"""def most_frequent_char(s):
    s = s.lower()          # Convert to lowercase
    freq = {}

    # Count character frequencies (ignore spaces)
    for ch in s:
        if ch != " ":
            freq[ch] = freq.get(ch, 0) + 1

    max_count = 0
    result = ""

    # Find the most frequent character
    # First one wins in case of a tie
    for ch in s:
        if ch != " " and freq[ch] > max_count:
            max_count = freq[ch]
            result = ch

    return result


# Test Cases
print(most_frequent_char("Hello World"))   # l
print(most_frequent_char("Suraj Sharma"))  # a
print(most_frequent_char("aabbcc"))        # a
print(most_frequent_char("Python"))        # p
print(most_frequent_char("AAAbbB"))        # a"""