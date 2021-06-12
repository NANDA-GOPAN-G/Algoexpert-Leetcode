"""
Following is a program that uses all of the insertion methods to create a linked list.
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self,prev_node,new_value):
        if prev_node is None:
            print("Previous node must be in LinkedList")
            return
        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self,new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next

llist = LinkedList()

llist.append(6)
llist.push(7)
llist.push(1)
llist.append(4)
llist.insertAfter(llist.head.next,8)

llist.printlist()
