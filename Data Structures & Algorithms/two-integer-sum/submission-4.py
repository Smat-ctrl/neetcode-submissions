class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differenceHashMap = defaultdict(int)
        # [3,4,5,6] => target 7
        indices = []

        # (key, value) = > (difference_value, idx)
        for i in range(len(nums)): # O(n)
            complement = target - nums[i]
            if complement in differenceHashMap:
                return [differenceHashMap[complement], i]
            differenceHashMap[nums[i]] = i
        
        return []
        

        # (4, 5, 6): differenceHashMap = (6 | 0), (5 | 1),  


        

                
        
        