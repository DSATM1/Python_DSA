
###----- Pseudocode----#####
# largest = first element of list
# for each number in list:
#     if number > largest:
#         largest = number       ← update largest, not number
# return largest


####------Code-----#####
lst = [3,9,7,5,14,0]

largest = lst[0]

for item in lst:
    if item > largest:
        largest = item
print(largest)  


