"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
  
Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
"""
Time Complexity = O(n) | Space complexity = O(n)
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr = []
        row_begin = 0
        row_end = len(matrix)-1
        column_begin = 0
        column_end = len(matrix[0])-1
        while row_end>=row_begin and column_end>=column_begin:
            for i in range(column_begin,column_end+1):
                arr.append(matrix[row_begin][i])

            for i in range(row_begin+1,row_end+1):
                arr.append(matrix[i][column_end])

            for i in range(column_end-1,column_begin-1,-1):
                if row_begin == row_end:
                    break
                arr.append(matrix[row_end][i])

            for i in range(row_end-1,row_begin,-1):
                if column_begin == column_end:
                    break
                arr.append(matrix[i][column_begin])

            column_begin += 1
            column_end -= 1
            row_begin += 1
            row_end -= 1

        return arr
