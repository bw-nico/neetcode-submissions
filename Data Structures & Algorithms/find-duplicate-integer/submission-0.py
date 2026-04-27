class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash = {}
        for num in nums:
            if hash.get(num):
                return num
            else:
                hash[num] = True