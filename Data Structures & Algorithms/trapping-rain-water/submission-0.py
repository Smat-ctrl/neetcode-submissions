class Solution:
    def trap(self, height: List[int]) -> int:

        maxLeft = 0
        maxLeft_arr = [0] * len(height)

        maxRight_arr = [0] * len(height)
        maxRight = 0
        min_arr = [0] * len(height)

        countBlocks = 0
        for i in range(len(height)):
            if maxLeft > height[i]:
                maxLeft_arr[i] = maxLeft
            else:
                maxLeft_arr[i] = height[i]
                maxLeft = height[i]
        
        for i in range(len(height) - 1, -1, -1):
            if maxRight > height[i]:
                maxRight_arr[i] = maxRight
            else:
                maxRight_arr[i] = height[i]
                maxRight = height[i]

        for i in range(len(height)):
            min_arr[i] = min(maxLeft_arr[i], maxRight_arr[i])
        
        for i in range(len(height)):
            if min_arr[i] - height[i] >= 0:
                countBlocks += (min_arr[i] - height[i])

        return countBlocks
                
            
            
            