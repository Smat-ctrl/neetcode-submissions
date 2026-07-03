class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        length = r
        max_area = 0

        while l < r:
            min_height = min(heights[l], heights[r])
            temp_area = length * min_height

            if temp_area > max_area:
                max_area = temp_area
            
            if heights[l] > heights[r]:
                r -=1
            else:
                l += 1
            length -= 1
        
        return max_area
