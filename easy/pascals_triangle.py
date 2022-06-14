"""
Link: https://leetcode.com/problems/pascals-triangle/
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = [[1]]
        numRows -= 1
        while numRows:
            prev_row = l[-1]
            new_row = [0] * (len(prev_row) + 1)
            new_row[0], new_row[-1] = 1, 1
            if len(new_row) > 2:
                for i in range(1, len(new_row) - 1):
                    new_row[i] = prev_row[i - 1] + prev_row[i]
            l.append(new_row)
            numRows -= 1
        return l
