"""
Link: https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        res_l = None
        res_r = None
        for i in range(len(s)):
            # odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > max_len:
                    max_len = curr_len
                    res_l = l
                    res_r = r
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > max_len:
                    max_len = curr_len
                    res_l = l
                    res_r = r
                l -= 1
                r += 1
        return s[res_l:res_r + 1]
