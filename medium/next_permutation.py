"""
Link: https://leetcode.com/problems/next-permutation/
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        e.g. for [1, 2, 3]
        123
        132
        213
        231
        312
        321
        
        k! - dup combos
        what's the current ith combo, and what's the next non-dupe one?
        """
        nums_sorted = sorted(nums)
        nums_sorted_copy = list(nums_sorted)
        alternatives_at_each_n = []
        empty_alternatives = 0
        for n in nums:
            alternatives = [x for x in nums_sorted_copy if x > n]
            if len(alternatives) == 0:
                empty_alternatives += 1
            alternatives_at_each_n.append(alternatives)
            nums_sorted_copy.pop(nums_sorted_copy.index(n))
        if empty_alternatives == len(nums):
            i, j = 0, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        else:
            for i, alternatives in enumerate(alternatives_at_each_n):
                if len(alternatives) != 0:
                    i_to_use = i
                    
            i = i_to_use

            j = 0
            while j < len(nums):
                if j < i:
                    nums_sorted.pop(nums_sorted.index(nums[j]))
                elif j == i:
                    nums[j] = min(alternatives_at_each_n[i])
                    nums_sorted.pop(nums_sorted.index(nums[j]))
                else:
                    nums[j] = nums_sorted.pop(0)
                j += 1
