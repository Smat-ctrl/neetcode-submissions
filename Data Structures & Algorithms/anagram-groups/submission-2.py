class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charMap = defaultdict(tuple)
        res = []
        idx = 0
        for i in range(len(strs)):
            # O(1) since there is a constraint of chars being at most length 100
            val = tuple(sorted(strs[i]))
            # End of O(1)
            if val in charMap:
                res[charMap[val]].append(strs[i])
            else:
                charMap[val] = idx
                idx += 1
                res.append([strs[i]])
        return res
                


