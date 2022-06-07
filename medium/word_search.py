"""
Link: https://leetcode.com/problems/word-search/
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""


from typing import List


class Solution:
    def dfs(self, y, x, word, board):
        if len(word) == 0:
            return True
        if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]) or word[0] != board[y][x]:
            return False
        temp = board[y][x]
        board[y][x] = '#'
        result = (
            self.dfs(y + 1, x, word[1:], board) or
            self.dfs(y - 1, x, word[1:], board) or
            self.dfs(y, x + 1, word[1:], board) or
            self.dfs(y, x - 1, word[1:], board)
        )
        board[y][x] = temp
        return result
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        x = 0
        y = 0
        
        m = len(board)
        n = len(board[0])
        curr_letter = word[0]
        word_indices = []
        for y in range(len(board)):
            for x in range(len(board[0])):
                if self.dfs(y, x, word, board):
                    return True
        return False
