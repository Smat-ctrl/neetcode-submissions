class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = defaultdict(int)
        hashMapT = defaultdict(int)

        if len(s) != len(t):
            return False

        # (key, value) => (character, # of occurences)
        for c in s:
            hashMapS[c] += 1
        
        for c in t:
            hashMapT[c] += 1
        
        for key, value in hashMapS.items():
            if value != hashMapT[key]:
                return False
        
        return True

        
