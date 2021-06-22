"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
"""
"""
Time Complexity:O(n) | Space Cmplexity:O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        d = {}
        i =  0
        for j in range(0,len(s)):
            
            if s[j] in d:
                i = max(i, d[s[j]]+1)
                
            res = max((j-i+1),res)
            d[s[j]] = j
                
        return res
