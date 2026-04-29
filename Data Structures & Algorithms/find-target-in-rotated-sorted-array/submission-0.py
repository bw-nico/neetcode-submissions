class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r: # Use <= to ensure we check the last remaining element
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # Identify which half is sorted
            # Case 1: Left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1 # Target is in the sorted left half
                else:
                    l = mid + 1 # Target is in the right half
            
            # Case 2: Right half is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1 # Target is in the sorted right half
                else:
                    r = mid - 1 # Target is in the left half
        return -1
