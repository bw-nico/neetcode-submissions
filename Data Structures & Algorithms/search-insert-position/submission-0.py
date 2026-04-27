class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Target is in the right half, move left boundary
                left = mid + 1
            else:
                # Target is in the left half, move right boundary
                right = mid - 1
                
        # If not found, 'left' will naturally be at the insertion index
        return left