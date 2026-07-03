class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        # dvdf
        # zxyzxyz
        # xxxx
        # pwwkew
        charMap = {}
        l = 0
        counter = 0
        maxVal = 0
        while l < len(s):
            c = s[l]
            if c in charMap:
                if c == s[l - 1]:
                    maxVal = max(maxVal, counter)
                    charMap.clear()
                    charMap[c] = l
                    counter = 1
                else:
                    l = charMap[c] + 1
                    maxVal = max(maxVal, counter)
                    counter = 0
                    charMap.clear()
                    continue
            else:
                charMap[c] = l
                counter += 1
            l += 1
        return max(maxVal, counter)
            
