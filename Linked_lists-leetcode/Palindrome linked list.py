"""
Given the head of a singly linked list, return true if it is a palindrome.

 
Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""
"""
Time Complexity: O(n)  |  Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        
        # to find middle eleme(slow)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reversing the second half of list
        prev = None
        
        while slow:
            slow.next,prev,slow = prev,slow,slow.next
        
        #check paliandrome
        left,right = head,prev
        
        while right:  # we can use either this or we can use "while left.next"
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
