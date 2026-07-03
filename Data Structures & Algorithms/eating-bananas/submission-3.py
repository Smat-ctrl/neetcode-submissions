class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search on the range of values
        l = 1
        r = max(piles)
        currentMin = r
        while l <= r:
            mid = int((l + r) / 2)
            counter = 0
            # count whether the k value is correct
            for i in range(len(piles)):
                counter += math.ceil(piles[i] / mid)
            
            if counter <= h:
                currentMin = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return currentMin
        