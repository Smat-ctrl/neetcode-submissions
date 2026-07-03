class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap1 = defaultdict(int)
        res = []

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashmap1:
                res.append(hashmap1[difference])
                res.append(i)
                break
            hashmap1[nums[i]] = i
        return res
