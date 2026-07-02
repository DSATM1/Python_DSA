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

## Line-by-Line Explanation
"""
```python
def most_frequent_char(s):
```

Creates a function named `most_frequent_char`.

```python
s = s.lower()
```

Converts all letters to lowercase.

Example:

```text
"Hello World" → "hello world"
```

```python
freq = {}
```

Creates an empty dictionary to store character frequencies.

```python
for ch in s:
```

Loops through every character.

```python
if ch != " ":
```

Ignores spaces.

```python
freq[ch] = freq.get(ch, 0) + 1
```

Counts each character.

Example:

```text
hello

h → 1
e → 1
l → 2
o → 1
```

Dictionary:

```python
{'h':1, 'e':1, 'l':2, 'o':1}
```

---

```python
max_count = 0
result = ""
```

Keeps track of:

* `max_count` → highest frequency found
* `result` → most frequent character

---

```python
for ch in s:
```

Loops through the string again in its original order.

```python
if ch != " " and freq[ch] > max_count:
```

If the current character has a strictly higher frequency than any seen before, update the answer.

Using `>` (not `>=`) ensures that if two characters have the same frequency, the first one encountered remains the result.

```python
max_count = freq[ch]
result = ch
```

Updates the current best answer.

---

```python
return result
```

Returns the most frequent character.

---

## Dry Run

Input:

```text
"Hello World"
```

After lowercase:

```text
hello world
```

Frequency dictionary:

```python
{
'h':1,
'e':1,
'l':3,
'o':2,
'w':1,
'r':1,
'd':1
}
```

Second loop:

| Character | Count | max_count | Result |
| --------- | ----: | --------: | ------ |
| h         |     1 |         1 | h      |
| e         |     1 |         1 | h      |
| l         |     3 |         3 | l      |
| l         |     3 |         3 | l      |
| o         |     2 |         3 | l      |
| ...       |   ... |       ... | l      |

Final answer:

```text
l
```

### Time Complexity

* **O(n)** — one pass to count frequencies and one pass to find the answer.

### Space Complexity

* **O(k)** — where `k` is the number of distinct characters in the string."""
