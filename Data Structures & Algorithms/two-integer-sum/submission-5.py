class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differenceMap = defaultdict(int)
        res = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in differenceMap:
                res.append(differenceMap[difference])
                res.append(i)
                break
            differenceMap[nums[i]] = i
        return res
        

            