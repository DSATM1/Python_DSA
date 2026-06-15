#complexity analysis

"""#O(1) #no matter how much big the list is the work is only in first attemplt only 
lst = [23,43,54,65,76,87,98,100]
print(lst[0])"""


"""#O(log(n)) in this we should sort the list before printing otherwise it will return -1
def find_name(book, target):
    left = 0
    right = len(book) - 1
    while left <= right:
        mid = (left + right)//2
        if book[mid] == target:
            return mid
        elif book[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
book = ["Suraj","Shobha","Sridhar","Supritha","Gaurav", "Vishnu"]
book.sort()
#print(find_name(book,"Sridhar"))

t_name= "Supritha"
res = find_name(book,t_name)
if res != -1:
    print(f"{t_name} Found at index {res}")
else:
    print("Not Found")"""


