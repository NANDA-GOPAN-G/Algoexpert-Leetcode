"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        for a in range(len(nums)-2):
            if a>0 and nums[a] == nums[a-1]:
                continue
            lt = a + 1
            rt = len(nums)-1
            while lt < rt:
                if nums[a]+nums[lt]+nums[rt] == 0:
                    arr.append([nums[a],nums[lt],nums[rt]])
                    while lt<rt and nums[lt] == nums[lt+1]:
                        lt = lt+1
                    while lt<rt and nums[rt] == nums[rt-1]:
                        rt = rt-1
                    lt = lt + 1
                    rt = rt - 1
                elif nums[a]+nums[lt]+nums[rt] < 0:
                    lt = lt + 1
                else:
                    rt = rt - 1
        return arr
