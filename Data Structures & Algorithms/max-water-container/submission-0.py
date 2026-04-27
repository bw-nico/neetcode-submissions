class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_vol = 0
        while l < r:
            volume = min(heights[l],heights[r]) * (r-l)
            max_vol = max(max_vol,volume)
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return max_vol
        