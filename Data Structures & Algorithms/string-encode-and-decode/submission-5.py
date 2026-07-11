class Solution:

    def encode(self, strs: List[str]) -> str:
        # 5Hello5World => HelloWorld,WorldHello => 10#HelloWorld10#WorldHello
        res = ""
        for i in range(len(strs)):
            length = str(len(strs[i]))
            res = res + length + "#" + strs[i]
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#": #10
                j += 1
            
            length = int(s[i:j])

            start = j + 1
            end = start + length

            res.append(s[start:end])
            i = end
        
        return res
            


