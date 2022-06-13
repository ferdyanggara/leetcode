"""
Link: https://leetcode.com/problems/combination-sum/
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""
class Solution:     
    def depthFirstSearch(self, candidates: List[int], remaining_target: int, current_combination: List[int], all_current_combos: List[List[int]]) -> List[int]:
        if remaining_target == 0:
            return current_combination
        elif remaining_target < 0:
            return None
        else:
            for i in range(len(candidates)):
                result = self.depthFirstSearch(candidates[i:], remaining_target - candidates[i], current_combination + [candidates[i]], all_current_combos)
                if result:
                    all_current_combos.append(result)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        all_current_combos = []
        self.depthFirstSearch(candidates, target, [], all_current_combos)
        return all_current_combos
