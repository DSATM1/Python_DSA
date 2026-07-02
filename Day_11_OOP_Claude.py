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








"""This problem is about **dictionaries + tuples + loops + arithmetic**.

### Approach

1. Create an empty dictionary to store each item's revenue.
2. Initialize a variable `total = 0`.
3. Loop through each record `(item, price, quantity)`.
4. Calculate revenue:

   ```python
   revenue = price * quantity
   ```
5. Add the revenue to the corresponding item.
6. Add the revenue to the overall total.
7. After the loop, add `"total"` to the dictionary.

---

## Python Code

```python
def sales_summary(records):
    summary = {}
    total = 0

    for item, price, quantity in records:
        revenue = price * quantity

        summary[item] = summary.get(item, 0) + revenue
        total += revenue

    summary["total"] = total
    return summary


# Test Data
records = [
    ("apple", 10, 3),
    ("banana", 5, 6),
    ("apple", 10, 2),
    ("banana", 5, 4),
]

print(sales_summary(records))
```

---

## Output

```python
{
    'apple': 50,
    'banana': 50,
    'total': 100
}
```

---

# Line-by-Line Explanation

### Function Definition

```python
def sales_summary(records):
```

Creates a function that accepts a list of sales records.

---

### Empty Dictionary

```python
summary = {}
```

Stores the revenue of each item.

Example:

```python
{
    "apple": 50,
    "banana": 50
}
```

---

### Overall Revenue

```python
total = 0
```

Keeps track of the total revenue from all items.

---

### Loop Through Records

```python
for item, price, quantity in records:
```

Each tuple is unpacked into:

```python
("apple", 10, 3)

item = "apple"
price = 10
quantity = 3
```

---

### Calculate Revenue

```python
revenue = price * quantity
```

Example:

```python
10 × 3 = 30
```

---

### Add Revenue to Item

```python
summary[item] = summary.get(item, 0) + revenue
```

The `get()` method returns the current revenue for the item, or `0` if it doesn't exist.

**First record**

```python
summary = {}

summary["apple"] = 0 + 30
```

Result:

```python
{
    "apple": 30
}
```

**Third record**

```python
summary["apple"] = 30 + 20
```

Result:

```python
{
    "apple": 50
}
```

---

### Update Total Revenue

```python
total += revenue
```

Example:

```
30
30 + 30 = 60
60 + 20 = 80
80 + 20 = 100
```

---

### Add Total to Dictionary

```python
summary["total"] = total
```

Dictionary becomes:

```python
{
    "apple": 50,
    "banana": 50,
    "total": 100
}
```

---

### Return Result

```python
return summary
```

Returns the final dictionary.

---

# Dry Run

### Initial Values

```python
summary = {}
total = 0
```

### Iteration 1

```python
("apple", 10, 3)

revenue = 30

summary = {
    "apple": 30
}

total = 30
```

---

### Iteration 2

```python
("banana", 5, 6)

revenue = 30

summary = {
    "apple": 30,
    "banana": 30
}

total = 60
```

---

### Iteration 3

```python
("apple", 10, 2)

revenue = 20

summary = {
    "apple": 50,
    "banana": 30
}

total = 80
```

---

### Iteration 4

```python
("banana", 5, 4)

revenue = 20

summary = {
    "apple": 50,
    "banana": 50
}

total = 100
```

---

### Final Result

```python
{
    "apple": 50,
    "banana": 50,
    "total": 100
}
```

---

## Time Complexity

* **O(n)**, where `n` is the number of records (each record is processed once).

## Space Complexity

* **O(k)**, where `k` is the number of unique items stored in the dictionary."""