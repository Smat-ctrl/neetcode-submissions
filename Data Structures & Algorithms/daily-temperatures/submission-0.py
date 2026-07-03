class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 
        stack = []
        res = [0] * len(temperatures)
        length = len(temperatures)

        for i in range(len(temperatures)):
            stack.append(temperatures[i])

        for i in range (len(temperatures)):
            current = temperatures[i]
            j = i
            total = 0
            while j <= (length - 1):
                if current < temperatures[j]:
                    res[i] = total
                    break
                total += 1
                j += 1
        
        return res
                