class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = set(nums)

        longest = 0
        for i in range(len(nums)):
            
            if nums[i] - 1 not in set_of_nums:
                val = nums[i]
                length = 0
                while val in set_of_nums:
                    length += 1
                    val += 1
                longest = max(length, longest)
        return longest
                