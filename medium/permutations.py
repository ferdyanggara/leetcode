"""
Link: https://leetcode.com/problems/permutations/
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from typing import List


class Solution:
    def permuteRecursive(self, nums: List[int], permutation: List[int], all_permutations: List[List[int]]):
        if len(nums) == 1:
            permutation.append(nums.pop())
            return permutation, all_permutations + [permutation]
        else:
            for n in nums:
                remaining_nums = [n_i for n_i in nums if n_i != n]
                new_permutation, all_permutations = self.permuteRecursive(remaining_nums, permutation + [n], all_permutations)
            return new_permutation, all_permutations

    def permute(self, nums: List[int]) -> List[List[int]]:
        _, all_permutations = self.permuteRecursive(nums, [], [])
        return all_permutations