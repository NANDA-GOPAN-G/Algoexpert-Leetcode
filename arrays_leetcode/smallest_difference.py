"""
write a program that takes in two non-empty array of integers.
The function should find the pair of numbers (one from the first array, one from the second array) whose absolute difference is closest to zero.
The function should return an array containing these two numbers, with the number from the first array in the first position.

Assume that there will be one pair of numbers with the smallest difference.
Sample input: nums1 = [-1,5,10,20,28,3], nums2 = [26,134,135,15,17]
Sample output: [28,26]
"""

"""
SOLUTION 1: time complexity is O(mn)
SOLUTION 2: time complexity is O(mlog(m) + nlog(n))
"""

"""SOLUTION 1"""
def smallest_diff(nums1:list[int] , nums2:list[int]) -> list[int]:
    a = 0
    b = 0
    diff = float("inf")
    ar = []

    while a<len(nums1):
        s = abs(nums1[a]-nums2[b])
        if s < diff:
            diff = s
            ar[0:2] = nums1[a],nums2[b]
            b = b + 1
        else:
            b = b + 1
        if b == len(nums2):
            a = a + 1
            b = 0
    return ar

num1 = list(map(int,input("Enter the values of first array seperated by spaces: ").split(" ")))
num2 = list(map(int,input("Enter the values of second array seperated by spaces: ").split(" ")))
print(smallest_diff(num1,num2))

"""_____________________________________________________________________________________________________________________________"""

"""SOLUTION 2"""
def smallest_diff(nums1:list[int] , nums2:list[int]) -> list[int]:
    a = 0
    b = 0
    diff = float("inf")
    ar = []
    
    while a<len(nums1):
        s = abs(nums1[a]-nums2[b])
        if nums1[a] < nums2[b]:
            a += 1
        elif nums1[a] > nums2[b]:
            b += 1
        else:
            return [nums1[a],nums2[b]]
        if s < diff:
            diff = s
            ar[0:2] = nums1[a],nums2[b]
            
    return ar

num1 = list(map(int,input("Enter the values of first array seperated by spaces: ").split(" ")))
num2 = list(map(int,input("Enter the values of second array seperated by spaces: ").split(" ")))
print(smallest_diff(num1,num2))

