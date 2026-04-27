class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        size = min(len(s) for s in strs)
        ret_val = ''
        should_break = False
        while count < size:
            check_char = strs[0][count]
            for each in strs:
                if each[count] != check_char:
                    should_break = True
                    break
            if should_break:
                break
            ret_val += check_char
            count +=1
        return ret_val