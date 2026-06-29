# 5 13 15 7 6
# Second Largest 
# CPU thinking level 

# Step 1 = we need to read the all numbers one by one 
# Step 2 = assume the first number is largest so largest = 5 
# Step 3 = read the bext bumber   largest = 13
# Step 4 = compare new value which is (13) to the cureent value which is (5) if the new value is > current value then update and remember the largest value is 13(new value)
# Step 5 = read the next number (15) and again compare with current largest value (13) if it's > then copy to largest if that is success then copy the largest to second largest.
# Step 6 = read next number (7) if it's smaller no action to be taken if it's greater than largest then update 
# Step 7 = read next number (6) same as above if it's greater take the action else no action to be taken 


# 19 5 13 15 7 6

# first valu is greater 

# read = 19->5->13->15->7->6

# largest = 19->19->19->19->19->19

# sec_larg =  0->5->13->15->15->15


"""def second_larg(numbers):
    largest = 0
    second_largest = 0
    #largest = numbers[0]
    for num in numbers:
        if num >= largest:
            second_largest = largest
            largest = num
        elif num >= second_largest:
            second_largest = num
    return second_largest

print(second_larg([51,13,15,61,7]))"""