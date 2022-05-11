"""
Link: https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_order = []
        for c in s:
            if c == '(':
                bracket_order.append(')')
            elif c == '{':
                bracket_order.append('}')
            elif c == '[':
                bracket_order.append(']')
            elif c == ')':
                if len(bracket_order) > 0 and bracket_order[-1] == ')':
                    bracket_order.pop()
                else:
                    return False
            elif c == ']':
                if len(bracket_order) > 0 and bracket_order[-1] == ']':
                    bracket_order.pop()
                else:
                    return False
            elif c == '}':
                if len(bracket_order) > 0 and bracket_order[-1] == '}':
                    bracket_order.pop()
                else:
                    return False
        if len(bracket_order) != 0:
            return False
        return True