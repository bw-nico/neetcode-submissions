class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1] * len(nums)
        right_product = [1] * len(nums)
        running_prod = 1
        for idx, num in enumerate(nums):
            if idx == len(nums) - 1:
                break
            running_prod*=num
            left_product[idx+1] = running_prod
        running_prod = 1
        for i in range(len(nums) - 1, 0, -1):
            running_prod *= nums[i]
            # The product of elements to the right of (i-1) is running_prod
            right_product[i - 1] = running_prod
        x = 1
        res = []
        for i in range(len(nums)):
            res.append(left_product[i]*right_product[i])
        return res

        