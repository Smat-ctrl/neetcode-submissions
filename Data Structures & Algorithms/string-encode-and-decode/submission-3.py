class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs)):
            seperator = str(len(strs[i]))
            result += (seperator + "#" + strs[i])
        return result

    # 5#Hello5#World => 
    def decode(self, s: str) -> List[str]:
        res = []
        length = 0
        i = 0
        while i < len(s):
            j = i
            temp = ""
            while s[j] != "#":
                temp += s[j]
                j += 1
            length = int(temp)
            word = s[j + 1: j + 1 + length]
            i = j + 1 + length
            res.append(word)
        return res
