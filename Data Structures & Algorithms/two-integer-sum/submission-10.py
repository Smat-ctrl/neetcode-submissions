class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[nums[i]] = i

        return []

        # iterations:
        # diff = 4, is 4 in the hashmap, no nothing in the hashmap => hashmap[3] = 0, i = 0
        # diff = 3, is 3 in the hashmap, yes its in the hashmap retunr 0, 1