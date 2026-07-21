class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxArea = 0

        while i < j:
            heightMin = min(heights[i], heights[j])
            length = abs(i - j)
            area = length * heightMin

            if area > maxArea:
                maxArea = area
            
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return maxArea
