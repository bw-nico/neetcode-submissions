class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_map = {}
        for num in nums:
            if seen_map.get(num):
                return True
            else:
                seen_map[num] = True
        return False