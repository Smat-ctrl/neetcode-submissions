class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1 = {}
        h2 = {}
        l = 0

        for c in s1:
            if c in h1:
                h1[c] += 1
            else:
                h1[c] = 1
        
        for r in range(len(s2)):
            c = s2[r]
            if c in h2:
                h2[c] += 1
            else:
                h2[c] = 1
            
            if r + 1 - l == len(s1):
                if h1 == h2:
                    return True
                h2[s2[l]] -= 1
                if h2[s2[l]] == 0:
                    del h2[s2[l]]
                l += 1
        return False
        