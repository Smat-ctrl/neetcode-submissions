class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setOfNums = set(nums)
        maxLen = 0

        for i in range(len(nums)):
            number = nums[i]
            length = 0
            while number in setOfNums:
                number -= 1
                length += 1
            
            if length > maxLen:
                maxLen = length
        
        return maxLen


