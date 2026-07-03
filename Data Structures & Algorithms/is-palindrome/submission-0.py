class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed = ""
        fixed = ""
        for i in range(len(s) - 1, -1, -1):
            if (s[i] >= "A" and s[i] <= "Z") or (s[i] >= "a" and s[i] <= "z") or (s[i] >= "0" and s[i] <= "9"):
                reversed += s[i]

        for i in range(len(s)):
            if (s[i] >= "A" and s[i] <= "Z") or (s[i] >= "a" and s[i] <= "z") or (s[i] >= "0" and s[i] <= "9"):
                fixed += s[i]

        return reversed.lower() == fixed.lower()