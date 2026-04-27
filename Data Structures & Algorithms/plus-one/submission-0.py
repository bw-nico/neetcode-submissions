class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_num = ''
        return_sum = []
        for each in digits:
            str_num += str(each)
        str_sum = str(int(str_num) + 1)
        for each in str_sum:
            return_sum.append(each)
        return return_sum

        