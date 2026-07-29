# ═══════════════════════════════════════════════════════
#  Problem  : 0001. Two Sum
#  URL      : https://leetcode.com/problems/two-sum/submissions/2086712605/
#  Difficulty : Easy
#  Language : Python3
#  Runtime  : 0 ms
#  Memory   : 20.5 MB
#  Solved   : July 29, 2026
# ═══════════════════════════════════════════════════════

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, n in enumerate(nums):
            res = target - n
            if res in table:
                return [table[res], i]
            table[n] = i