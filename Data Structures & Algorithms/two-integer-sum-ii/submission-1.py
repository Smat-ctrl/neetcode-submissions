class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l = 0
        r = len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                res.append(l + 1)
                res.append(r + 1)
                return res
            if total <= target:
                l += 1
            if total >= target:
                r -= 1
        return res