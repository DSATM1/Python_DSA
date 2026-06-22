#---Searching And Sorting -----


# Bubble Sort
"""def sortArray(nums):
    n = len(nums)

    for i in range(n):
        isSwap = False
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                isSwap = True
        if not isSwap:
            break
    
    return nums    
    
print(sortArray([32,43,1,56,98,9,32312,787,112,9866]))"""



# Insertion Sort

"""def sortArray(nums):
        n = len(nums)

        for i in range(1,n):
            key = nums[i]
            j = i-1
            while j >=0 and nums[j]>key:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key

        return nums

print(sortArray([89,43,12,56,78,32]))"""