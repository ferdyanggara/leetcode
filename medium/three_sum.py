"""
Link: https://leetcode.com/problems/3sum/
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = []
        length = len(nums)
        if length < 3:
            return []
        for i_1 in range(length - 2):
            if i_1 > 0 and nums[i_1] == nums[i_1 - 1]:
                continue
            i_2, i_3 = i_1 + 1, length - 1
            while i_2 < i_3:
                num_sum = nums[i_1] + nums[i_2] + nums[i_3]
                if num_sum > 0:
                    i_3 -= 1
                elif num_sum < 0:
                    i_2 += 1
                else:
                    triplets.append([nums[i_1], nums[i_2], nums[i_3]])
                    i_3 -= 1
                    while i_2 < i_3 and nums[i_3] == nums[i_3 + 1]:
                        i_3 -= 1

        return triplets