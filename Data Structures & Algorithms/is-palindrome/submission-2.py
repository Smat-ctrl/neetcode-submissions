class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and self.isalphNum(s[l]) == False:
                l += 1
            while r > l and self.isalphNum(s[r]) == False:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True



    def isalphNum(self, s: str) -> bool:
        if (s >= "A" and s <= "Z") or (s >= "a" and s <= "z") or (s >= "0" and s <= "9"):
            return True
        return False