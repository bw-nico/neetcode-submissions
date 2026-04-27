class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for idx, num in enumerate(nums):
            check = target - num
            if check in seen_map:
                return [seen_map[check], idx]
            else:
                seen_map[num] = idx