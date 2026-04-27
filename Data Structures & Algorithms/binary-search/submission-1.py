class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            center = (right + left)//2
            if nums[center] == target:
                return center
            elif nums[center] < target:
                left = center + 1
            elif nums[center] > target:
                right = center - 1
        return -1
        