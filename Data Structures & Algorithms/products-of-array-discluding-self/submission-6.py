class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

        # [1,2,4,6] => [1, ], p = 1 => [1,1], p = 2 => [1,1,2,8]
        # [1,1,2,8], [1,2,4,6] => [1,1,2,8],pt=6 => [1,1,12,8] pt=24 =>[1,24,12,8] pt=48 => [48,24,12,8]
