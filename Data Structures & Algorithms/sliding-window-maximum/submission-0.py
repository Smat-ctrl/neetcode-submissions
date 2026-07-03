class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []
        l = 0

        for r in range(len(nums)):
            if nums[r] in hashmap:
                hashmap[nums[r]] += 1
            else:
                hashmap[nums[r]] = 1
            
            if r - l + 1 == k:
                res.append(max(hashmap.keys()))
                hashmap[nums[l]] -= 1
                if hashmap[nums[l]] == 0:
                    del hashmap[nums[l]]
                l += 1
        return res

            
            
            
        