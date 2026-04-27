from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurrence = defaultdict(int)
        for letter in s:
            occurrence[letter] +=1
        for letter in t:
            occurrence[letter] -=1
        for key in occurrence.keys():
            if occurrence[key] != 0:
                return False
        return True