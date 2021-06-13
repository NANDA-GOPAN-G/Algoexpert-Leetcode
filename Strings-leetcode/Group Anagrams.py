"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""
"""
Time Complexity: O(mnlogn)  |  Space Complexity: O(mn)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in groups:
                groups[sorted_word].append(word)
            else:
                groups[sorted_word] = [word]
        
        return groups.values()
                
