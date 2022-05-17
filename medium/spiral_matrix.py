"""
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        y_min, x_min = 0, 0
        y_max = len(matrix) - 1
        x_max = len(matrix[0]) - 1

        nums = []
        while x_min <= x_max and y_min <= y_max:
            for x in range(x_min, x_max + 1):
                nums.append(matrix[y_min][x])
            y_min += 1

            for y in range(y_min, y_max + 1):
                nums.append(matrix[y][x_max])
            x_max -= 1
            if y_min <= y_max:  # needs this check here so we don't double iterate
                for x in range(x_max, x_min - 1, -1):
                    nums.append(matrix[y_max][x])
            y_max -= 1

            if x_min <= x_max:  # needs this check here so we don't double iterate
                for y in range(y_max, y_min - 1, -1):
                    nums.append(matrix[y][x_min])
            x_min += 1
        return nums