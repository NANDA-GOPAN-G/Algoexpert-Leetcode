"""Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem using only constant extra space.

 

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [1,1]
Output: 1

Example 4:
Input: nums = [1,1,2]
Output: 1
"""

"""
Time Complexity: O(n)  |  Space Complexity: O(1)
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for value in nums:
            abs_value = abs(value)
            if nums[abs_value - 1] < 0:
                return abs_value
            nums[abs_value - 1] *= -1
        return -1
