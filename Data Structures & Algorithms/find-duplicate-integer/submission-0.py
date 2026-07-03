class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set_of_nums = set()

        for i in range(len(nums)):
            if nums[i] in set_of_nums:
                return nums[i]
            set_of_nums.add(nums[i])
        return 0