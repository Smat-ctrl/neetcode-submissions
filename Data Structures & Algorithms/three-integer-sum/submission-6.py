class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            idx1 = i + 1
            idx2 = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while idx1 < idx2:
                target = nums[i] + nums[idx1] + nums[idx2]

                if target == 0:
                    res.append([nums[i], nums[idx1], nums[idx2]])
                    idx1 += 1
                    idx2 -= 1

                    while idx1 < idx2 and nums[idx1] == nums[idx1 - 1]:
                        idx1 += 1
                    
                    while idx1 < idx2 and nums[idx2] == nums[idx2 + 1]:
                        idx2 -= 1
                    

                elif target > 0:
                    idx2 -= 1
                else:
                    idx1 += 1
        
        return res



