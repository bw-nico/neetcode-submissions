class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        for each in strs:
            if "".join(sorted(each)) not in ana_dict:
                ana_dict["".join(sorted(each))] = [each]
            else:
                ana_dict["".join(sorted(each))].append(each)
        ret = []
        for key in ana_dict.keys():
            ret.append(ana_dict[key])
        return ret