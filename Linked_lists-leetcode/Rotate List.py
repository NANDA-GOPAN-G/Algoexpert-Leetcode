"""
Given the head of a linked list, rotate the list to the right by k places.


Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""
"""
Time Complexity: O(n)  |  Space Complexity:  O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        
        last = head
        count = 1
        
        while last.next:
            last = last.next
            count += 1
            
        last.next = head
        k = k % count
        curr = head
        
        for k in range(count-k-1):
            curr = curr.next
            
        res = curr.next
        curr.next = None
        
        return res
