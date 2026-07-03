class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum_of_both = nums[l] + nums[r]
                if sum_of_both == target:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    continue
                if sum_of_both < target:
                    l += 1
                if sum_of_both > target:
                    r -= 1
        return res


