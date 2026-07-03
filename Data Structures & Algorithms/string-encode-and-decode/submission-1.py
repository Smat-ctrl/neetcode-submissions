class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs)):
            seperator = str(len(strs[i]))
            result += (seperator + "#" + strs[i])
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":  # find the delimiter
                j += 1
            length = int(s[i:j])            # read the length
            word = s[j+1 : j+1+length]      # jump exactly length chars
            result.append(word)
            i = j + 1 + length              # move i to next word
        return result


        





                




