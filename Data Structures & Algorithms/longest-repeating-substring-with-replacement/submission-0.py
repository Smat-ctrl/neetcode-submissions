class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    
        hashMap = {}
        l = 0
        res = 0
        for r in range(len(s)):
            maxVal = 0
            if s[r] in hashMap:
                hashMap[s[r]] += 1
            else:
                hashMap[s[r]] = 1

            for items in hashMap:
                maxVal = max(maxVal, hashMap[items])
            
            while (r - l + 1) - maxVal > k:
                hashMap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res




        
        