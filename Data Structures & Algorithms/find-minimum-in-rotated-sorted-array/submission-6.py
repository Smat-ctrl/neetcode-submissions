class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minVal = nums[0]
        while l <= r:
            mid = (l + r) // 2
            minVal = min(minVal, nums[mid])
            if l == r:
                break
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return minVal