class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characterHash1 = defaultdict(int)
        characterHash2 = defaultdict(int)

        if len(s) != len(t):
            return False

        for c in s:
            characterHash1[c] += 1
        
        for c in t:
            characterHash2[c] += 1


        for key in characterHash1:
            if characterHash1[key] != characterHash2[key]:
                return False
        
        return True