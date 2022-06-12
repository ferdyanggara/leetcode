"""
Link: https://leetcode.com/problems/3sum-closest/submissions/
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
 

Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""
class Solution:
    def delta(self, value: int, target: int):
        return abs(value - target)

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        smallest_delta = 2e31 - 1
        smallest_i = 0
        smallest_j = 1
        smallest_k = 2
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                sums_delta = self.delta(sums, target)
                if sums_delta < smallest_delta:
                    smallest_delta = sums_delta
                    smallest_i = i
                    smallest_j = j
                    smallest_k = k
                if sums > target:
                    k -= 1
                elif sums < target:
                    j += 1
                else:
                    return target
        return nums[smallest_i] + nums[smallest_j] + nums[smallest_k]
