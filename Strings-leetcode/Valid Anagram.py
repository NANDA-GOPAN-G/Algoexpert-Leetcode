"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""
"""
Time Complexity: O(mlogm+nlogn)  |  Space Complexity: O(m+n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_t = "".join(sorted(t))
        sorted_s = "".join(sorted(s))
        if sorted_s == sorted_t:
            return True
        else:
            return False
