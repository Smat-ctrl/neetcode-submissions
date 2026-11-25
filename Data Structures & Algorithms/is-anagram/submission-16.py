class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmapS = {}
        hashmapT = {}

        for c in s:
            hashmapS[c] = hashmapS.get(c, 0) + 1
        
        for c in t:
            hashmapT[c] = hashmapT.get(c, 0) + 1

        for c in s:
            if hashmapS.get(c) != hashmapT.get(c):
                return False
        
        return True
