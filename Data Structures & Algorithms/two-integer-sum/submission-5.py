class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lucky_number = {}
        for idx, val in enumerate(nums):
            lucky = target - val
            if lucky in lucky_number:
                return [lucky_number[lucky],idx]
            lucky_number[val] = idx
        