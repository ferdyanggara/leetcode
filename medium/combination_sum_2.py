"""
Link: https://leetcode.com/problems/combination-sum-ii/
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
class Solution:
    def depthFirstSearch(self, candidates: List[int], remaining_target: int, current_combination: List[int], all_current_combos: List[List[int]]) -> List[int]:
        if remaining_target == 0:
            all_current_combos.append(current_combination)
            return
        
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining_target:
                break
                
            self.depthFirstSearch(candidates[i + 1:], remaining_target - candidates[i], current_combination + [candidates[i]], all_current_combos)
            

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        all_current_combos = []
        candidates.sort()
        self.depthFirstSearch(candidates, target, [], all_current_combos)
        return all_current_combos
