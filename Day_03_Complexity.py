#------Complexity Analysis-------



"""# O(n) Linear Time 
n = 5
for i in range(n):
    print(i, end = " ")
m = 3
for i in range(n+m):
    print(i, end = " ")"""


"""# Constant Time O(1)
# In this case it dosen't depend on input the input will be constant 
for i in range(100):
    print(i,end = " ")"""


"""# Quadratic O(n^2) Multiple conditions 
# And when u have O(n) or O(1) and O(n^2) then u can say like O(n^2) bcz the the one condition is big and one is small
n = 5
for i in range(n):
    for j in range(n):
        print(i,j, end = " ")

for i in range(n):
    print(i,end = " ")"""

"""# Logerthm Time O(log n)
# when u have multiplication and division then this will be applied 

for i in range(n*=2):
    print(i)

while i <=n:
    print(n)
    n//=2"""