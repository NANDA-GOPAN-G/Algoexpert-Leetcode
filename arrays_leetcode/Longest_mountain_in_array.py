"""
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.


Example 1:
Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:
Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.
"""

"""
Time Complexity: O(n)  |  Space Complexity: O(1)
"""

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        cnt = 0
        
        for peak in range(1,len(arr) - 1):
            if arr[peak - 1] < arr[peak] > arr[peak + 1]:
                
                left = right = peak
                
                while left > 0 and arr[left] > arr[left-1]:
                    left -= 1
                
                while right + 1 < len(arr) and arr[right] > arr[right+1]:
                    right += 1
                
                cnt = max(cnt,(right-left+1))
                
        return cnt
