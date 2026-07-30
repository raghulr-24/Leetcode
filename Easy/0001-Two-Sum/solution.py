# ═══════════════════════════════════════════════════════
#  Problem  : 0001. Two Sum
#  URL      : https://leetcode.com/problems/two-sum/
#  Difficulty : Easy
#  Language : Python3
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : July 30, 2026
# ═══════════════════════════════════════════════════════

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in table:
                return [table[i], n]
        table[i] = n
        