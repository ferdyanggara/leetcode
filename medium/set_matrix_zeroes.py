"""
Link: https://leetcode.com/problems/set-matrix-zeroes/submissions/
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_with_zeros = set()
        cols_with_zeros = set()
        n = len(matrix)
        m = len(matrix[0])
        
        first_row_has_zero = False
        first_col_has_zero = False
        
        for y in range(n):
            for x in range(m):
                if matrix[y][x] == 0:
                    if x == 0:
                        first_col_has_zero = True
                    if y == 0:
                        first_row_has_zero = True
                    matrix[y][0] = 0
                    matrix[0][x] = 0
                
                
        for y in range(1, n):
            for x in range(1, m):
                if matrix[y][0] == 0 or matrix[0][x] == 0:
                    matrix[y][x] = 0
        if first_row_has_zero:
            for x in range(m):
                matrix[0][x] = 0
        if first_col_has_zero:
            for y in range(n):
                matrix[y][0] = 0
