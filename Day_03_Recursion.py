#-----Recursion-----

"""def printNum(i,n):
    if i>n:
        return
    print(i,end = " ")
    printNum(i+1, n)

printNum(0,5)"""



# Factorial of n
"""def fact(n):
    if n <= 0:
        return 1
    return n*fact(n-1)
print(fact(5))"""


#----GCD-----
"""def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)
print(gcd(10,15))"""

"""def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

def lcm(a,b):
    return a*b//gcd(a,b)
print(gcd(10,15))
print(lcm(10,15))"""