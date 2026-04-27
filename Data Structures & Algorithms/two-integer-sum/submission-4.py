class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            check = target - num
            if check in hash_map:
                return [hash_map[check], i]
            else:
                hash_map[num] = i