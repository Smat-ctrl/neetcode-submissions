class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmapS = defaultdict(int)
        hashmapT = defaultdict(int)

        for c in s:
            hashmapS[c] += 1
        
        for c in t:
            hashmapT[c] += 1

        for c in s:
            if hashmapS[c] != hashmapT[c]:
                return False
        
        return True
