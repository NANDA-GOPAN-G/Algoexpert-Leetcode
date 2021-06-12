"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = ""
        a = 0
        b = 0
        while(b<len(t)):
            if a == len(s):
                break
            if s[a] == t[b]:
                l += t[b]
                a = a + 1
                b = b + 1
            else:
                b = b + 1
        """
        for understanding below piece of code.
        if s == l:
            return True
        else:
            return False
        """
        return True if s == l else False
