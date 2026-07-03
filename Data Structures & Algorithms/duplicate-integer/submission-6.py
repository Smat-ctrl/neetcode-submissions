class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)

        for i in range(len(nums)):
            if hashmap[nums[i]] >= 1:
                return True
            hashmap[nums[i]] += 1
        
        return False