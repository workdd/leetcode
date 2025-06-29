class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = {}
        for s in strs:
            sorted_s = sorted(s)
            sorted_s = "".join(sorted_s)
            if sorted_s not in res_dict:
                res_dict[sorted_s] = [s]
            else:
                res_dict[sorted_s].append(s)
        res = list(res_dict.values())
        res = sorted(res)
        return res
