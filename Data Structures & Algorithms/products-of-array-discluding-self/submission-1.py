class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        for i in range(len(nums)):
            ignore = i
            multiplicand = 1
            for j in range(len(nums)):
                if j == ignore:
                    continue
                else:
                    multiplicand *= nums[j]
            result.append(multiplicand)
        return result




