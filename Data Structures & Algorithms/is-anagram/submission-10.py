class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMapS = defaultdict(int)
        charMapT = defaultdict(int)
        if len(s) != len(t):
            return False

        for c in s:
            charMapS[c] += 1
        
        for c in t:
            charMapT[c] += 1
        
        for items in charMapS:
            if items not in charMapT:
                return False
            if charMapS[items] != charMapT[items]:
                return False
        
        return True