class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = set(nums)
        longest = 0
        for i in range(len(nums)):

            if nums[i] - 1 not in set_of_nums:
                length = 1
                val = nums[i] + 1
                while val in set_of_nums:
                    length += 1
                    val += 1
                longest = max(longest, length)
        
        return longest
