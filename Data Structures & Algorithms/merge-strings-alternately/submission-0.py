class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        smallest = min(len(word1), len(word2)) - 1
        idx = 0
        ret = ''
        while idx <= smallest:
            ret += word1[0]
            ret += word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
            idx+=1
        if word1:
            ret += word1
        else:
            ret += word2
        return ret
        