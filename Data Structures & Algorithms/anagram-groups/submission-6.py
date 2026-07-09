class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(tuple)
        res = []
        idx = 0

        for i in range(len(strs)):
            word = tuple(sorted(strs[i]))# cab = > (c,a,b) => (a,b,c)
            if word in hashmap:
                res[hashmap[word]].append(strs[i])
            else:
                hashmap[word] = idx
                res.append([strs[i]])
                idx += 1
        
        return res






