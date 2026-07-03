class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(tuple)
        res = []
        idx = 0
        for i in range(len(strs)):
            val = tuple(sorted(strs[i]))
            if val in hashMap:
                res[hashMap[val]].append(strs[i])
            else:
                res.append([strs[i]])
                hashMap[val] = idx
                idx += 1
        
        return res

