class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charMap = defaultdict(list)
        res = []
        idx = 0
        for i in range(len(strs)):
            val = tuple(sorted(strs[i]))
            if val in charMap:
                res[charMap[val]].append(strs[i])
            else:
                charMap[val] = idx
                idx += 1
                res.append([strs[i]])
        
        return res
