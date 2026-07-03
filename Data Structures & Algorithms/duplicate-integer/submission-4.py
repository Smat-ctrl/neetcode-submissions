class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)

        #(key, value) => (value of nums at i, # of occurences)
        for i in range (len(nums)):
            if (hashmap[nums[i]] >= 1):
                return True
            hashmap[nums[i]] += 1
        
        return False
