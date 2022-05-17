"""
Link: https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        max_sub = nums[0]
        for i in range(1, len(nums)):
            # clever trick here in which you add the last item of dp (which has the current item in the array)
            # only if the last item of dp is positive, meaning that it's a candidate for the max subarray
            dp.append(nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0))
            max_sub = max(max_sub, dp[i])
        return max_sub