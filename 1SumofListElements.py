
### sum of elements in list

def sums(i,n,total,l):
    if (i>=n):
        return total
    total+=l[i]
    return sums(i+1,n,total,l)
l=[10,20,30,40]
print(sums(0,4,0,l))

# Passing data from Parent function to child function
def printSum(index, n, nums, result):
    if index == n:
        print("Sum is:", result)
        return 
 
    result += nums[index]
    #result = result + nums[index]
    printSum(index + 1, n, nums, result)
 
# Passing data from child function to Parent function
def printSum2(index, n, nums):
    if index == n:
        return 0 
    nextElementsSum = printSum2(index + 1, n, nums)
    return nextElementsSum + nums[index]
 
nums = [12, 34, 12, 5, 7]
n = len(nums)
result = printSum2(0, n, nums)
print("Sum is:", result)


# maximum element
def m(i,n,maxelem,l):
    if (i>=n):
        return maxelem
    maxelem =max(maxelem,l[i])
    return m(i+1,n,maxelem,l)
l=[10,20,30,40]
maxelem=0
print(m(0,4,0,l))

