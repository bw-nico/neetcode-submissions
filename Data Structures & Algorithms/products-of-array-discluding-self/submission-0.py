class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count+=1
            else:
                product*=num
        ret = ['_']*len(nums)
        if zero_count > 1:
            return [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                ret[i] = product
            elif zero_count == 1:
                ret[i] = 0
            else:
                ret[i] = int(product/nums[i])
        return ret
        