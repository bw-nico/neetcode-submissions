class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        for idx, val in enumerate(nums):
            if val in mp:
                if k >= abs(mp[val] - idx):
                    return True
                else:
                    mp[val] = idx
            else:
                mp[val] = idx
        return False


        