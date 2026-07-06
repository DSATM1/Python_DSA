
###----- Pseudocode----#####
# largest = first element of list
# for each number in list:
#     if number > largest:
#         largest = number       ← update largest, not number
# return largest


####------Code-----#####
"""lst = [3,9,7,5,14,0]

largest = lst[0]

for item in lst:
    if item > largest:
        largest = item
print(largest)  
"""


###----- Pseudocode----#####
# create empty basket
# for each num in list:
#     if num % 2 == 0:
#         add num to basket    ← this line is inside the if
# return the basket

####------Code-----#####
"""lst = [12,2,3,4,5,6,7,8,9]
l1 = []
for i in lst:
    if i % 2 == 0:
        l1.append(i) #type:ignore
print(l1)"""




####------Code-----#####
"""lst = [1,8,2,4,9]
largest = lst[0]
for i in lst:
     if i > largest:
            largest = i
second_largest = lst[0]
for j in lst:
    if j > second_largest and j < largest:
          second_largest = j 
print(second_largest)"""
