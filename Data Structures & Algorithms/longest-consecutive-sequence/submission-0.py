class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in set_of_nums:
                length = 0
                temp = nums[i] + 1
                while temp in set_of_nums:
                    length += 1
                    temp += 1
                longest = max(longest, length + 1)
        return longest
            