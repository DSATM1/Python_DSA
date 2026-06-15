#complexity analysis

"""#O(1) #no matter how much big the list is the work is only in first attemplt only 
lst = [23,43,54,65,76,87,98,100]
print(lst[0])"""


"""Binary Search Function"""
"""#O(log(n)) in this we should sort the list before printing otherwise it will return -1 and it's faster than Linear
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



"""#O(n) Slower compared to Binary but it does not need sorting  
def find_paper(papers,name):
    for paper in papers:
        if paper == name:
            return True 
    return False
papers = ["Lucky","Madan","Sure","Devid","Mallu"]
print(find_paper(papers,"Devid"))
print(find_paper(papers,"Suman"))"""



"""#O(n^2)(n square) using multiple looping conditions 
def find_dup(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                return True 
            
    return False
numbers = [10,23,45,5,56]
print(find_dup(numbers))"""


"""#O(2^n) (2 to the power n) Worst case
def fib(n):
    if n < 2:
        return n 
    return fib(n -1) + fib(n - 2)
if __name__ == "__main__":
    for i in range(0,10):
        print(i, fib(i))"""