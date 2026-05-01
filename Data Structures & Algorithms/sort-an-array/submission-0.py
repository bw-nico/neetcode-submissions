class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)
    
    def merge(self, list1, list2):
        result = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                result.append(list1[i])
                i+=1
            else:
                result.append(list2[j])
                j+=1
        result.extend(list1[i:])
        result.extend(list2[j:])
        return result