"""
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].  An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Return true if and only if the given array nums is monotonic.

 

Example 1:
Input: nums = [1,2,2,3]
Output: true

Example 2:
Input: nums = [6,5,4,4]
Output: true

Example 3:
Input: nums = [1,3,2]
Output: false

Example 4:
Input: nums = [1,2,4,5]
Output: true

Example 5:
Input: nums = [1,1,1]
Output: true
"""

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = 0
        decrease = 0
        
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                increase += 1
            elif nums[i-1] > nums[i]:
                decrease += 1
        
        return increase==0 or decrease==0
