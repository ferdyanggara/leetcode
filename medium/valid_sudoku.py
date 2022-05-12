"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""
from typing import List


class Solution:
    BOARD_SIZE = 9

    def containsDuplicates(self, array: List[str]) -> bool:
        seen_numbers = set()
        for i in array:
            if i == '.':
                continue
            elif i in seen_numbers:
                return True
            else:
                seen_numbers.add(i)
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y in range(self.BOARD_SIZE):
            if self.containsDuplicates(board[y]):
                return False
        for x in range(self.BOARD_SIZE):
            if self.containsDuplicates([board[y][x] for y in range(self.BOARD_SIZE)]):
                return False
        for i in range(3):
            for j in range(3):
                y_index = [y + 3 * j for y in range(3)]
                x_index = [x + 3 * i for x in range(3)]
                sub_board = []
                for y in y_index:
                    for x in x_index:
                        sub_board.append(board[y][x])
                if self.containsDuplicates(sub_board):
                    return False
        return True