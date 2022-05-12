"""
Link: https://leetcode.com/problems/first-missing-positive/
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1


Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)  # need to append 0 so we have 1-index array instead of 0 indexed array
        n = len(nums)
        for i in range(len(nums)):
            if (nums[i] < 0 or  # check for negatives (self explanatory)
                    nums[i] >= n  # check for ints larger than n. the missing int is either between 1, ..., n -1 or n
            ):
                nums[i] = 0
        for i in range(len(nums)):
            nums[nums[
                     i] % n] += n  # using this hash algo, we're able to preserve the value in the original array and count if the value has been seen

        for i in range(1, len(nums)):
            if int(nums[i] / n) == 0:  # indexes where the value < n means they have not been seen
                return i
        return n