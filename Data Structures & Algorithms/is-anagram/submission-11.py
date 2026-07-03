class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS = defaultdict(int)
        hashmapT = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in s:
            hashmapS[i] += 1
        
        for j in t:
            hashmapT[j] += 1
        
        for j in hashmapS:
            if hashmapS[j] != hashmapT[j]:
                return False
        
        return True