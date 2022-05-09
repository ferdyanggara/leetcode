"""
Link: https://leetcode.com/problems/reverse-integer/
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        x_min = -2 ** 31
        x_max = 2 ** 31 - 1
        res = 0
        sign = 1 if x >= 0 else -1
        while x != 0:
            res *= 10
            res += x % (sign * 10)

            if res < x_min or res > x_max:
                return 0
            x = int(x / 10)
        return res