"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
"""
"""
Time Complexity: O(n) | Space complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        previous = None
        
        while head:
            temp_next = head.next
            head.next = previous
            previous = head
            if temp_next is None:
                break
            head = temp_next
        
        return previous
    
"""Much simplified code of above version"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        previous = None
        
        while head:
            head.next,previous,head = previous,head,head.next
        
        return previous
    
