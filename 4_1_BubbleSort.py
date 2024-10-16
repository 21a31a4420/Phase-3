
# iterative approach bubble sort
# a=[81,9,14,2]
# n=len(a)
# for i in range(0,n):
#     for j in range(0,n-i-1):
#         if a[j] > a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j] 
# print(a )


# recursive approach


def bubblesort(nums,n):
    if n==1:
        return
    # last index is n-1
    for index in range(n-1):
        if nums[index] > nums[index+1]:
            nums[index],nums[index+1] =nums[index+1],nums[index]
    bubblesort(nums,n-1)

def selectionsort(nums,n):
    if n==1:
        return
    # fix(n-1) index
    maxelemindx=n-1
    for index in range(n-1):
        if nums[index]>nums[maxelemindx]:
            maxelemindx=index
    if maxelemindx != n-1 :
        nums[maxelemindx],nums[n-1]= nums[n-1] ,nums[maxelemindx]

    selectionsort(nums,n-1)

def insertionsort(nums,n):
    if n==1:
        return
    insertionsort(nums,n-1)
    curval=nums[n-1]
    prevind=n-2
    while prevind >=0:
        if nums[prevind] > curval:
            nums[prevind+1] =nums[prevind]
        else:
            break
        prevind-=1
    nums[prevind+1]=curval

def mergeTwoArrays(nums,left,mid,right):
    temp=[]
    idx1=left
    idx2=mid+1
    while idx1 <= mid and idx2 <= right:
        if nums[idx1] > nums[idx2]:
            temp.append(nums[idx2])
            idx2 +=1
        else:
            temp.append(nums[idx1])
            idx1+=1
    while idx1 <= mid :
        temp.append(nums[idx1])
        idx1 +=1
    while idx2 <= right:
        temp.append(nums[idx2])
        idx2+=1
    pos=0
    for index in range(left,right+1):
        nums[index]=temp[pos]
        pos +=1 

def divideandMerge(nums,left,right):
    if left >= right:
        return
    mid =(left+right)//2
    # left subarray --> [left,mid]
    # right subarray --> [mid+1,right]
    divideandMerge(nums,left,mid)
    divideandMerge(nums,mid+1,right)
    mergeTwoArrays(nums,left,mid,right)

def mergesort(nums):
    n=len(nums)
    divideandMerge(nums,0,n-1)


# quicksort
# 1.find the pivots index after sorting
# 2.move all smaller elems to pivot lefts ,, and move all greater elems to pivots right

def getpivotindex(nums,left,right):
    if left >= right:
        return
    pivot=nums[right]
    # [18,12,22,23,10,7,20]
    # [18,12,10,22,23,7,20]
    # [18,12,10,7,22,23,20]
    # [18,12,10,7,22,23,20]
    # [18,12,10,7,20,22,23]
    pos=left
    for index in range(left,right):
        if nums[index]<pivot:
            nums[index],nums[pos]=nums[pos],nums[index]
            pos +=1
    nums[right]

def findPivotAndSort(nums,left,right):
    if left >= right:
        return
    
def quicksort(nums):
    n=len(nums)
    # quicksort(nums)
    findPivotAndSort(nums,0,n-1)
    
def countingsort(nums):
    n=len(nums)
    temp=[-1]*n
    m=max(nums)
    store=[0]*(m+1)
    for ele in nums:
        store[ele]+=1
    for id in range(1,n):
        store[id] += store[id-1]
    for id in range(n-1,-1,-1):
        ele=nums[id]
        store[ele]-=1
        temp[store[ele]]=ele
    for id in range(n):
        nums[id] = temp[id]
# nums = [8, 1, 7, 6, 5, 4, 3, 2, 1, 1, 2, 2, 4, 4, 4, 4, 6]

# nums=[8,1,7,6,5,4,3,2,10,-1,-5]
# bubblesort(nums,len(nums))
# print("after bubble sort:",nums)
# selectionsort(nums,len(nums))
# print("after selection sort:" , nums)
# insertionsort(nums,len(nums))
# print("after insertion sort:", nums)
# mergesort(nums)
# countingsort(nums)
# print(nums)  


# linear search
def ls(nums):
    t=4
    for i in ls:
        if i==t:
            return nums[i]
        else:
            return -1
# recursice linear search  

def linearsrch(nums,target,index,n):
    if index==n:
        return -1
    elif nums[index] == target:
        return index
    return linearsrch(nums,target,index+1,n)
# nums=[1,4,2,8,4,9]
# target=9
# index=linearsrch(nums,target,0,len(nums))
# if index ==-1:
#     print(target,"not found")
# else:
#     print(target , "found at index:" , index) 


# recursive binary search 
def binarysrch(nums,target,left,right):
    # n=len(nums)
    if left > right:
        return -1
    mid = (left+right)//2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binarysrch(nums,target,left,mid-1)
    
    return binarysrch(nums,target,mid+1,right)

# nums=[1,4,2,8,4,9]
# nums.sort()
# target=4
# index=binarysrch(nums,target,0,len(nums)-1)
# if index ==-1:
#     print(target,"not found")
# else:
#     print(target , "found at index:" , index) 

    
# 1.find 1st occurence of a target using binary search
# 2.find last occurence of a target using binary search
# 3.find total num of occurences of a target using binary search






def findFirstOccurrence(nums, target):
    n = len(nums)
    left, right = 0, n - 1 
    result = -1 
    while left <= right:
        mid = (left + right) // 2 
        if nums[mid] == target:
            result = mid 
            right = mid - 1 
        elif nums[mid] > target:
            right = mid - 1 
        else:
            left = mid + 1 
 
    return result
 
# nums = [1, 2, 3, 4, 4, 4, 4, 6, 7]
# print(findFirstOccurrence(nums, 4))
# print(findFirstOccurrence(nums, 7))
# print(findFirstOccurrence(nums, 41))


# def findFirstOccurrence(nums, target):
#     n = len(nums)
#     left, right = 0, n - 1 
#     result = -1 
#     while left <= right:
#         mid = (left + right) // 2 
#         if nums[mid] == target:
#             result = mid 
#             right = mid - 1 
#         elif nums[mid] > target:
#             right = mid - 1 
#         else:
#             left = mid + 1 
#     return result
 
# nums = [1, 2, 3, 4, 4, 4, 4, 6, 7]
# print(findFirstOccurrence(nums, 4))
# print(findFirstOccurrence(nums, 7))
# print(findFirstOccurrence(nums, 41))




# tasks to do :
# 1.merge two sorted list
# 2.merge k sorted list
# 3.swap nodes in pairs
# 4.reversing a linked list using recursion iterative
# 5.add two numvers
# 6.reverse nodes in k group
# 7.copy list with random pointer 


def swapPairs(self, head):
    if not head or not head.next:
        return head 

    dummyNode = ListNode(-1)
    tail = dummyNode 
    curr = head 
    while curr and curr.next:
        storeNext = curr.next.next 
        curr.next.next = curr 
        tail.next = curr.next 
        tail = curr 
        curr = storeNext 
    if curr:
        tail.next = curr 
    else:
        tail.next = None
    return dummyNode.next
