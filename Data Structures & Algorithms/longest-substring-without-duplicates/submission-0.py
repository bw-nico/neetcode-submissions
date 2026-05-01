class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        curr = ''
        longest = 0
        for idx, each in enumerate(s):
            if each not in curr:
                dic[each] = idx
                curr+=each
                if len(curr) > longest:
                    longest = len(curr)
            else:
                curr = curr.split(each)[1]
                curr+=each
                dic[each] = idx
        return longest
        