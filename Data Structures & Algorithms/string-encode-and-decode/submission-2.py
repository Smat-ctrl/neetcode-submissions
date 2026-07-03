class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        res = ""
        for i in range(len(strs)):
            word = strs[i]
            length = str(len(word))
            res += (length + "#" + word)
        return res


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            length = ""
            j = i
            while s[j] != "#":
                length += s[j]
                j += 1
            idx = int(length)
            res.append(s[j + 1:j + 1 + idx])
            i = j + 1 + idx
        return res

            
            

