class Solution:
    def check(self, h1, h2) -> bool:
        for items in h1:
            if items not in h2 or h2[items] < h1[items]:
                return False
        return True
    
    def minWindow(self, s: str, t: str) -> str:
        h1 = {}
        h2 = {}
        l = 0
        minSubstring = ""
        for c in t:
            if c in h1:
                h1[c] += 1
            else:
                h1[c] = 1
        
        for r in range(len(s)):
            contains = True
            c = s[r]
            if c in h2:
                h2[c] += 1
            else:
                h2[c] = 1

            if self.check(h1,h2) == False: # if not send back until we find one
                continue
            else:
                while self.check(h1,h2):
                    if minSubstring == "" or len(s[l:r+1]) < len(minSubstring):
                        minSubstring = s[l:r+1]
                    h2[s[l]] -= 1
                    if h2[s[l]] == 0:
                        del h2[s[l]]
                    l += 1
        return minSubstring

            
