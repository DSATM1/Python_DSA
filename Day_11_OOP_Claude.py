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













"""This problem tests your understanding of **Classes, Objects, Methods, Lists, and Conditional Statements**.

---

# Approach

1. Create a class named `Student`.
2. Use `__init__()` to initialize:

   * `name`
   * `marks` (an empty list)
3. Create `add_mark(mark)` to add marks to the list.
4. Create `get_average()` to calculate the average and round it to 2 decimal places.
5. Create `get_grade()` to return the grade based on the average.

---

# Python Code

```python
class Student:

    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def get_average(self):
        if len(self.marks) == 0:
            return 0
        return round(sum(self.marks) / len(self.marks), 2)

    def get_grade(self):
        average = self.get_average()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"


# Create Object
s = Student("Suraj")

# Add Marks
s.add_mark(88)
s.add_mark(92)
s.add_mark(79)

# Display Results
print("Name:", s.name)
print("Average:", s.get_average())
print("Grade:", s.get_grade())
```

---

# Output

```text
Name: Suraj
Average: 86.33
Grade: B
```

---

# Line-by-Line Explanation

## Create Class

```python
class Student:
```

Defines a class named `Student`.

---

## Constructor

```python
def __init__(self, name):
```

The constructor runs automatically when a new object is created.

Example:

```python
s = Student("Suraj")
```

Here:

* `self` → refers to the current object.
* `name` → `"Suraj"`.

---

## Store Name

```python
self.name = name
```

Stores the student's name.

Example:

```python
self.name = "Suraj"
```

---

## Empty Marks List

```python
self.marks = []
```

Creates an empty list for storing marks.

Initially:

```python
[]
```

---

## Add Marks Method

```python
def add_mark(self, mark):
```

Creates a method to add a mark.

```python
self.marks.append(mark)
```

Adds the mark to the list.

Example:

```python
s.add_mark(88)
```

Marks become:

```python
[88]
```

Then:

```python
s.add_mark(92)
```

Marks become:

```python
[88, 92]
```

Finally:

```python
s.add_mark(79)
```

Marks become:

```python
[88, 92, 79]
```

---

## Calculate Average

```python
def get_average(self):
```

Calculates the average marks.

```python
if len(self.marks) == 0:
    return 0
```

If no marks exist, return `0` to avoid division by zero.

---

```python
sum(self.marks)
```

Calculates the total.

Example:

```python
[88, 92, 79]

88 + 92 + 79 = 259
```

---

```python
len(self.marks)
```

Number of marks:

```python
3
```

---

```python
sum(self.marks) / len(self.marks)
```

Average:

```python
259 / 3 = 86.333333...
```

---

```python
round(..., 2)
```

Rounds the average to two decimal places.

Result:

```python
86.33
```

---

## Calculate Grade

```python
def get_grade(self):
```

Gets the student's grade based on the average.

```python
average = self.get_average()
```

Reuses the `get_average()` method instead of recalculating.

---

### Grade Conditions

```python
if average >= 90:
    return "A"
```

Average **90 or above** → Grade **A**.

```python
elif average >= 80:
    return "B"
```

Average **80–89.99** → Grade **B**.

```python
elif average >= 70:
    return "C"
```

Average **70–79.99** → Grade **C**.

```python
elif average >= 60:
    return "D"
```

Average **60–69.99** → Grade **D**.

```python
else:
    return "F"
```

Average **below 60** → Grade **F**.

---

# Dry Run

### Step 1

```python
s = Student("Suraj")
```

Object state:

```python
name = "Suraj"
marks = []
```

---

### Step 2

```python
s.add_mark(88)
```

Marks:

```python
[88]
```

---

### Step 3

```python
s.add_mark(92)
```

Marks:

```python
[88, 92]
```

---

### Step 4

```python
s.add_mark(79)
```

Marks:

```python
[88, 92, 79]
```

---

### Step 5

```python
s.get_average()
```

Calculation:

```text
88 + 92 + 79 = 259
259 / 3 = 86.333...
Rounded = 86.33
```

---

### Step 6

```python
s.get_grade()
```

Average:

```text
86.33
```

Condition check:

```text
86.33 >= 90 ❌
86.33 >= 80 ✅
```

Returns:

```text
"B"
```

---

## Time Complexity

* `add_mark(mark)`: **O(1)** (appending to a list).
* `get_average()`: **O(n)** (sums all marks).
* `get_grade()`: **O(n)** because it calls `get_average()`.

## Space Complexity

* **O(n)**, where `n` is the number of marks stored in the `marks` list."""













"""This problem helps you practice **Classes, Objects, Constructors (`__init__`), Instance Variables, and Methods**.

---

# Approach

1. Create a `BankAccount` class.
2. Initialize:

   * `owner`
   * `balance`
3. Create `deposit(amount)` to add money to the balance.
4. Create `withdraw(amount)` to subtract money if sufficient funds are available.
5. Create `get_balance()` to display the owner's name and current balance.

---

# Python Code

```python
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance after deposit: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Balance after withdrawal: ₹{self.balance}")

    def get_balance(self):
        print(f"Owner: {self.owner} | Balance: ₹{self.balance}")


# Create Object
acc = BankAccount("Suraj", 1000)

# Deposit Money
acc.deposit(500)

# Withdraw Money
acc.withdraw(200)

# Withdraw More Than Balance
acc.withdraw(2000)

# Check Balance
acc.get_balance()
```

---

# Output

```text
Balance after deposit: ₹1500
Balance after withdrawal: ₹1300
Insufficient funds
Owner: Suraj | Balance: ₹1300
```

---

# Line-by-Line Explanation

## Create the Class

```python
class BankAccount:
```

Defines a class named `BankAccount`.

---

## Constructor

```python
def __init__(self, owner, balance):
```

The constructor is called automatically when an object is created.

Example:

```python
acc = BankAccount("Suraj", 1000)
```

Here:

* `owner = "Suraj"`
* `balance = 1000`

---

## Store Owner Name

```python
self.owner = owner
```

Stores the account holder's name.

Result:

```text
owner = "Suraj"
```

---

## Store Balance

```python
self.balance = balance
```

Stores the starting balance.

Result:

```text
balance = 1000
```

---

## Deposit Method

```python
def deposit(self, amount):
```

Creates a method to deposit money.

```python
self.balance += amount
```

Adds the deposit amount to the balance.

Example:

```text
Current Balance = 1000
Deposit = 500

1000 + 500 = 1500
```

---

```python
print(f"Balance after deposit: ₹{self.balance}")
```

Displays the updated balance.

Output:

```text
Balance after deposit: ₹1500
```

---

## Withdraw Method

```python
def withdraw(self, amount):
```

Creates a method to withdraw money.

---

### Check for Sufficient Balance

```python
if amount > self.balance:
```

If the withdrawal amount is greater than the current balance:

```text
Balance = 1300
Withdraw = 2000
```

Since:

```text
2000 > 1300
```

Output:

```text
Insufficient funds
```

The balance remains unchanged.

---

### Successful Withdrawal

```python
else:
```

If enough balance exists:

```python
self.balance -= amount
```

Subtracts the amount.

Example:

```text
Balance = 1500
Withdraw = 200

1500 - 200 = 1300
```

---

```python
print(f"Balance after withdrawal: ₹{self.balance}")
```

Displays the updated balance.

Output:

```text
Balance after withdrawal: ₹1300
```

---

## Get Balance Method

```python
def get_balance(self):
```

Displays the owner's name and current balance.

```python
print(f"Owner: {self.owner} | Balance: ₹{self.balance}")
```

Output:

```text
Owner: Suraj | Balance: ₹1300
```

---

# Dry Run

### Step 1

```python
acc = BankAccount("Suraj", 1000)
```

Object state:

```text
Owner = "Suraj"
Balance = 1000
```

---

### Step 2

```python
acc.deposit(500)
```

Calculation:

```text
1000 + 500 = 1500
```

State:

```text
Balance = 1500
```

---

### Step 3

```python
acc.withdraw(200)
```

Calculation:

```text
1500 - 200 = 1300
```

State:

```text
Balance = 1300
```

---

### Step 4

```python
acc.withdraw(2000)
```

Check:

```text
2000 > 1300 ✔
```

Output:

```text
Insufficient funds
```

Balance remains:

```text
1300
```

---

### Step 5

```python
acc.get_balance()
```

Output:

```text
Owner: Suraj | Balance: ₹1300
```

---

# Final Object State

```python
{
    "owner": "Suraj",
    "balance": 1300
}
```

---

## Time Complexity

* `deposit(amount)`: **O(1)** — constant time.
* `withdraw(amount)`: **O(1)** — constant time.
* `get_balance()`: **O(1)** — constant time.

## Space Complexity

* **O(1)** — only two instance variables (`owner` and `balance`) are stored."""
