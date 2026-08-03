# ═══════════════════════════════════════════════════════
#  Problem  : 0152. Maximum Product Subarray
#  URL      : https://leetcode.com/problems/maximum-product-subarray/
#  Difficulty : Medium
#  Language : Python3
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : August 3, 2026
# ═══════════════════════════════════════════════════════

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cmin = 1
        cmax = 1
        for n in nums:
            temp = cmax*n
            cmax = max(temp, cmin*n, n)
            cmin = min(temp, cmin*n, n)
        res = max(res, cmax)
        return res
   

        