class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        j = len(numbers) - 1

        while i < j:
            sumNum = numbers[i] + numbers[j]
            if sumNum == target:
                return [i + 1, j + 1]
            if sumNum < target:
                i += 1
            if sumNum > target:
                j -= 1
        