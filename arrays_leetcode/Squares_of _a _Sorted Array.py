"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r = [None]*len(nums)
        p=len(nums)-1
        a=0
        b=len(nums)-1
        while a<=b:
            if nums[a]**2 < nums[b]**2:
                r[p]=nums[b]**2
                b = b-1
            else:
                r[p]=nums[a]**2
                a = a+1
            p = p-1
        return r
