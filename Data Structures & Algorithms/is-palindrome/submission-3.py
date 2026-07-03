class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        s = s.lower()
        
        for i in range(len(s) - 1, -1, -1):
            t += s[i]

        idxT = 0
        idxS = 0

        while idxT < len(t) and idxS < len(s):
            if not t[idxT].isalnum():
                idxT += 1
                continue
            if not s[idxS].isalnum():
                idxS += 1
                continue
            if s[idxS] != t[idxT]:
                return False
            
            idxS += 1
            idxT += 1

        return True