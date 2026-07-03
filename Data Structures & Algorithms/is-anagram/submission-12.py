class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashMapS = defaultdict(int)
        hashMapT = defaultdict(int)

        for c in s:
            hashMapS[c] += 1
        
        for c in t:
            hashMapT[c] += 1
        
        for key in hashMapS:
            if hashMapS[key] != hashMapT[key]:
                return False
        
        return True