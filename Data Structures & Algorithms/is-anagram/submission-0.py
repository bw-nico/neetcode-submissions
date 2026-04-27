class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        for each in s:
            if hash1.get(each):
                hash1[each] += 1
            else:
                hash1[each] = 1
        for each in t:
            if hash1.get(each):
                hash1[each] -= 1
            else:
                return False
        for key in hash1.keys():
            if hash1.get(key) != 0:
                return False
        return True