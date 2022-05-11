"""
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                mid_l = mid
                mid_r = mid

                while l < mid_l:
                    mid_l_1 = (l + mid_l) // 2
                    if nums[mid_l_1] < target:
                        if mid_l_1 + 1 <= mid_l:
                            l = mid_l_1 + 1
                        else:
                            l = mid_l
                    else:
                        if mid_l_1 - 1 >= l and nums[mid_l_1 - 1] == target:
                            mid_l = mid_l_1 - 1
                        else:
                            l = mid_l_1
                            mid_l = l

                while r > mid_r:
                    mid_r_1 = (r + mid_r) // 2
                    print(mid_r, mid_r_1, r)
                    if nums[mid_r_1] > target:
                        if mid_r_1 - 1 >= mid_r:
                            r = mid_r_1 - 1
                        else:
                            r = mid_r
                    else:
                        if mid_r_1 + 1 <= r and nums[mid_r_1 + 1] == target:
                            mid_r = mid_r_1 + 1
                        else:
                            r = mid_r_1
                            mid_r = r
                return [l, r]
        return [-1, -1]