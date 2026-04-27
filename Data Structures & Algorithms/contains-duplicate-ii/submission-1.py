class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        start, end = 0, min(k,len(nums) -1)
        while start < end and end <= len(nums) - 1:
            if nums[start] == nums[end]:
                return True
            elif end == start + 1:
                start+=1
                end = start + k
            else:
                end-=1
        return False


        