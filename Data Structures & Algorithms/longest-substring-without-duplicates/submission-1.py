class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = ''
        longest = 0
        for idx, each in enumerate(s):
            if each not in curr:
                curr+=each
                if len(curr) > longest:
                    longest = len(curr)
            else:
                curr = curr.split(each)[1]
                curr+=each
        return longest
        