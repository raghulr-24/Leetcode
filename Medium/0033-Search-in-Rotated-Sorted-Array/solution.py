# ═══════════════════════════════════════════════════════
#  Problem  : 0033. Search in Rotated Sorted Array
#  URL      : https://leetcode.com/problems/search-in-rotated-sorted-array/
#  Difficulty : Medium
#  Language : Python3
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
#  Solved   : August 2, 2026
# ═══════════════════════════════════════════════════════

class Solution:
    def search(self, nums: List[int], target: int) -> int:
         n = len(nums)
         l = 0
         r = n -1
         while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
         min = nums[r]