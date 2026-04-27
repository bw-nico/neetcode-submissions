class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_map = {}
        if len(s) != len(t):
            return False
        for letter in s:
            if letter_map.get(letter):
                letter_map[letter] += 1
            else:
                letter_map[letter] = 1
        for letter in t:
            if letter_map.get(letter):
                letter_map[letter] -= 1
            else:
                return False
        for key in letter_map.keys():
            if letter_map[key] != 0:
                return False
        return True
        