"""
Link: https://leetcode.com/problems/group-anagrams/
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_letters_dict = {}
        for s in strs:
            s_sorted = ''.join(list(sorted(s)))
            if s_sorted not in sorted_letters_dict:
                sorted_letters_dict[s_sorted] = []
            sorted_letters_dict[s_sorted].append(s)
        if len(sorted_letters_dict) == 0:
            sorted_letters_dict[''] = ['']
        return list(sorted_letters_dict.values())