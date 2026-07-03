class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.minSearch(nums, 0, len(nums) - 1)


    def minSearch(self, nums: List[int], l: int, r: int) -> int:
        if l == r:
            return nums[l]
        if r - l == 1:
            return min(nums[l], nums[r])

        mid = int((l + r) / 2)
        minimumLeft = self.minSearch(nums, l, mid)
        minimumRight = self.minSearch(nums, mid + 1, r)
        
        return min(minimumLeft, minimumRight)
        
        