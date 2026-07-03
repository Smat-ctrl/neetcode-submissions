class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                res = mid
                break

            if nums[mid] >= nums[l]: # if the number at mid is less than the number at l then check
                if target >= nums[l] and target <= nums[mid]: # if target is greater that l and less than that mid 
                    r = mid - 1
                else: # if not it should be on the right side
                    l = mid + 1
            else: # if the mid is not greater than the left we must check the right
                if target <= nums[r] and target > nums[mid]: # if the target is less than the right and greater then the mid 
                    l = mid + 1
                else:
                    r = mid - 1
        
        return res