"""def password_validator(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False

correct_password = "Tiger@123"
attempts = 3

while attempts > 0:
    pwd = input("Enter password: ").strip()

    if password_validator(pwd) and pwd == correct_password:
        print("✅ Access granted!")
        break
    else:
        attempts -= 1

        if attempts > 0:
            print(f"❌ Wrong! {attempts} attempts left.")
        else:
            print("🔒 Account locked!")"""


# Another way of PWD checker
"""correct_password = "tiger123"
attempts = 3

while attempts > 0:
    pwd = input("Enter password: ").strip()

    if pwd == correct_password:
        print("✅ Access granted!")
        break
    else:
        attempts -= 1

        if attempts > 0:
            print(f"❌ Wrong! {attempts} attempts left.")
        else:
            print("🔒 Account locked!")"""


"""def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

def lcm(a,b):
    return a*b//gcd(a,b)
print(gcd(10,15))
print(lcm(10,15))"""

"""def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary = ""

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    return binary


num = int(input("Enter decimal number: ").strip())

print(decimal_to_binary(num))"""


"""def count_occurrences(lst, target):
    count = 0

    for item in lst:
        if item == target:
            count = count + 1

    return count


print(count_occurrences([1, 2, 2, 3, 2], 2))
print(count_occurrences(["a", "b", "a", "c"], "a"))
print(count_occurrences([1, 2, 5, 5, 2], 5))"""


"""def sum_of_squares_loop(n):
    total = 0

    for i in range(1, n + 1):
        total = total + (i * i)

    return total


n = int(input("Enter n: ").strip())

print(sum_of_squares_loop(n))"""


"""def sum_of_squares_list_comprehension(n):
    return sum([i * i for i in range(1, n + 1)])


n = int(input("Enter n: ").strip())

print(sum_of_squares_list_comprehension(n))"""



"""def find_unique_pairs(lst, target):
    seen = set()
    pairs = set()

    for num in lst:
        needed = target - num

        if needed in seen:
            pair = tuple(sorted((num, needed)))
            pairs.add(pair)

        seen.add(num)

    return list(pairs)


print(find_unique_pairs([1, 5, 7, -1, 5], 6))
print(find_unique_pairs([1, 2, 3, 4, 5, 6], 7))"""