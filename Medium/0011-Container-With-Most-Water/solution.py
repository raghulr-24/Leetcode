# ═══════════════════════════════════════════════════════
#  Problem  : 0011. Container With Most Water
#  URL      : https://leetcode.com/problems/container-with-most-water/?difficulty=EASY&page=1
#  Difficulty : Medium
#  Language : Python3
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : August 1, 2026
# ═══════════════════════════════════════════════════════

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        maxarea = 0
        while l<r:
            x =  r - l
            y = min(height[l], height[r])
            area = x*y
            maxarea = max(maxarea, area)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maxarea    