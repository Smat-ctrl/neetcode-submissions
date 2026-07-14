class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setOfNums = set(nums)
        maxLen = 0

        for num in setOfNums:
            if (num - 1) not in setOfNums:
                current = num
                length = 0

                while current in setOfNums:
                    length += 1
                    current += 1
            
                if length > maxLen:
                    maxLen = length
        return maxLen
            

