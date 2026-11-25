class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(tuple)
        res = []
        idx = 0
        for i in range(len(strs)):
            val = tuple(sorted(strs[i]))
            if val in hashmap:
                res[hashmap[val]].append(strs[i])
            else:
                hashmap[val] = idx
                idx += 1
                res.append([strs[i]])
        return res
                
