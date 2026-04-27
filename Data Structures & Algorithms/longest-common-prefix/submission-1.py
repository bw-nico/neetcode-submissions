class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        size = min(len(s) for s in strs)
        ret_val = ''
        while count < size:
            check_char = strs[0][count]
            for each in strs:
                if each[count] != check_char:
                    return ret_val
            ret_val += check_char
            count +=1
        return ret_val