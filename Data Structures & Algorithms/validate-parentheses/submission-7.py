class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
    
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
                continue
            if s[i] == ")" or s[i] == "}" or s[i] == "]":
                if not stack:
                    return False
                val = stack.pop()
                if s[i] == ")":
                    if val != "(":
                        return False
                if s[i] == "}":
                    if val != "{":
                        return False
                if s[i] == "]":
                    if val != "[":
                        return False
                continue
            else:
                return False
        if stack:
            return False  
        return True
                