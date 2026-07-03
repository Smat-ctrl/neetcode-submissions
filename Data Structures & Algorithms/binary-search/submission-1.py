class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        mid = (len(nums) - 1) // 2
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid - 1
                l += 1
                mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
                r -= 1
                mid = (l + r) // 2
        return -1
        