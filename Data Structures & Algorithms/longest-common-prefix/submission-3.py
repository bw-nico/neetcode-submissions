class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        size = min(len(s) for s in strs)
        while count < size:
            check_char = strs[0][count]
            for each in strs:
                if each[count] != check_char:
                    return strs[0][0:count]
            count +=1
        return strs[0][0:count]