class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val = set(nums)
        return len(val) != len(nums)
        