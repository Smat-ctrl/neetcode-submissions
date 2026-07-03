class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = set(nums)
        max_consec = 0
        for i in range(len(nums)):
            j = nums[i]
            temp_counter = 0
            while j in set_of_nums:
                j -= 1
                temp_counter += 1
            max_consec = max(max_consec, temp_counter)
        
        return max_consec
