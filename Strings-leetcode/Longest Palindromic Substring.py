"""
Given a string s, return the longest palindromic substring in s.


Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
"""
"""
Time Complexity: O(n^2)  |  Space Complexity: O(n)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLength = 0
        
        for i in range(len(s)):
            
            #odd lenght
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLength:
                    res = s[l:r+1]
                    resLength = r - l + 1 
                l -= 1
                r += 1
            
            #even length
            l,r = i,i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLength:
                    res = s[l:r+1]
                    resLength = r - l + 1 
                l -= 1
                r += 1
            
        return res
