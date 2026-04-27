class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_map = {}
        for each in s:
            if each not in anagram_map:
                anagram_map[each] = 1
            else:
                anagram_map[each] +=1

        for each in t:
            if each not in anagram_map:
                return False
            else:
                anagram_map[each] -=1

        for key in anagram_map.keys():
            if anagram_map[key] != 0:
                return False
        return True
        