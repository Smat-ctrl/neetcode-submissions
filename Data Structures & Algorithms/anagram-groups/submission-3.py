class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      charMap = defaultdict(tuple)
      idx = 0
      res = []
      for i in range(len(strs)):
        current = tuple(sorted(strs[i])) # O(1) since 26 characters
        if current in charMap:
            res[charMap[current]].append(strs[i])
        else:
            charMap[current] = idx
            idx += 1
            res.append([strs[i]])

      return res