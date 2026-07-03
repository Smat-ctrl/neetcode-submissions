class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(tuple)
        returnList = []
        for i in range(len(strs)):
            sublist = []
            check = tuple(sorted(strs[i]))
            if check in hashMap:
                returnList[hashMap[check]].append(strs[i])
            else:
                sublist.append(strs[i])
                hashMap[check] = len(returnList)
                returnList.append(sublist)

        return returnList
            

