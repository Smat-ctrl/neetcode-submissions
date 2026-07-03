class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}


        for i in range(len(nums)):
            targetDif = target - nums[i]
            if targetDif in hashMap:
                return[hashMap[targetDif], i]
            else:
                hashMap[nums[i]] = i
    
        return 


        

                
        
        