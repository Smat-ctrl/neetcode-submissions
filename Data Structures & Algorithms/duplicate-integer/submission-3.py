class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)
        for items in nums:
            if hashmap[items] >= 1:
                return True
            else:
                hashmap[items] += 1
        return False
