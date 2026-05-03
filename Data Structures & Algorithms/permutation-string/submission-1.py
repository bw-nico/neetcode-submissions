class Solution:
    def checkInclusion(self, s2: str, s1: str) -> bool:
        left = 0
        right = len(s2) - 1
        s2_dict = {}
        if len(s2) > len(s1):
            return False
        for each in s2:
            if each not in s2_dict:
                s2_dict[each] = 1
            else:
                s2_dict[each] +=1
        while right < len(s1):
            sub_s1 = s1[left:right+1]
            sub_s1_dict = {}
            for each in sub_s1:
                if each not in sub_s1_dict:
                    sub_s1_dict[each] = 1
                else:
                    sub_s1_dict[each] +=1
            if sub_s1_dict == s2_dict:
                return True
            else:
                left+=1
                right+=1
        return False
        