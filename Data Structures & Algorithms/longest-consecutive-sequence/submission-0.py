class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        if not nums:
            return 0
        nums.sort()
        for num in nums:
            if num - 1 in dic:
                dic[num] = dic[num-1] + 1
            else:
                dic[num] = 1
        largest = 0
        for length in dic.values():
            largest = max(length,largest)
        return largest

        