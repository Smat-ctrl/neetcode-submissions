class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        containsDuplicate = defaultdict(int)

        for i in range(len(nums)):
            if containsDuplicate[nums[i]] >= 1:
                return True
            
            containsDuplicate[nums[i]] += 1
        
        return False