class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            sumOfNum = numbers[i] + numbers[j]

            if sumOfNum == target:
                return [i + 1, j + 1]
            
            if sumOfNum < target:
                i += 1
            
            if sumOfNum > target:
                j -= 1
        