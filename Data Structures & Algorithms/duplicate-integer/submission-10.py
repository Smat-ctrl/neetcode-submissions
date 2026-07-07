class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums));
        # [1,2,3,3] (4) => [1,2,3] (3)