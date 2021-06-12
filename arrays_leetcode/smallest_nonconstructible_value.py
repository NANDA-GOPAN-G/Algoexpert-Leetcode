"""
Given an array of positive integers (representing coins), find the smallest value that cannot be constructed from those integers.
Examples are given below.

Input: A = [1, 2, 4]
Output: 8
Explanation: With subsets of A, we can construct values 1, 2, 3, 4, 5, 6, 7.


Input: A = [1, 2, 5]
Output: 4
Explanation: With subsets of A, we can construct values 1, 2, 3, 5, 6, 7, 8.
"""

l = list(map(int,input("enter the values with spaces:").split(" ")))
s = 0 #smallest number is set a zero at first
l.sort()
for i in range(len(l)):
    if l[i] > s+1:
        print("the number is: ", s+1)
    elif l[i] == l[len(l)-1]:
        print("the number is: ",sum(l)+1)
    else:
        s = s + l[i]
