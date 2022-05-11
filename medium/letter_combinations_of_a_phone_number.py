"""
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from typing import List


class Solution:
    def addLettersToLetterList(self, letters_to_add: str, letter_list: List[str]) -> List[str]:
        if len(letter_list) == 0:
            return [letter_to_add for letter_to_add in letters_to_add]
        letter_list_to_return = []
        for letter in letter_list:
            for letter_to_add in letters_to_add:
                letter_list_to_return.append(letter + letter_to_add)
        return letter_list_to_return

    def letterCombinations(self, digits: str) -> List[str]:
        number_letter_dict = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        letter_list = []
        for d in digits:
            letters = number_letter_dict[int(d)]
            letter_list = self.addLettersToLetterList(letters, letter_list)
        return letter_list