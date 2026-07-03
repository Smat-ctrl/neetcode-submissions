class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            res = res + "#" + str(len(strs[i])) + "#" + strs[i]
        return res

    def decode(self, s: str) -> List[str]:
        number = ""
        idx = 0
        res = []

        while idx < len(s):
            if s[idx] == "#":
                idx += 1
                number = ""

                while s[idx] != "#":
                    number += s[idx]
                    idx += 1

                length = int(number)
                idx += 1

                res.append(s[idx: idx + length])
                idx += length

        return res