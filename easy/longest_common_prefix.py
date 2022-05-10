"""
Link: https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""


from typing import List


class Solution:
    def allCharactersEqual(self, i: int, strs: List[str]) -> bool:
        c = None
        for s in strs:
            if i >= len(s):
                return False
            if c is None:
                c = s[i]
            elif s[i] != c:
                return False
        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        s = ''
        while True:
            if self.allCharactersEqual(i, strs):
                s += strs[0][i]
                i += 1
            else:
                return s
