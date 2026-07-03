class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            maxVal1 = heapq.heappop_max(stones)
            maxVal2 = heapq.heappop_max(stones)
            if maxVal1 == maxVal2:
                continue
            if maxVal2 < maxVal1:
                newVal = maxVal1 - maxVal2
                heapq.heappush_max(stones, newVal)

        return stones[0] if len(stones) == 1 else 0
            
            
            