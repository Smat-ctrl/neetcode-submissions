class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minDistance = []
        res = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            euclideanDist =  math.sqrt(x**2 + y**2)
            minDistance.append((euclideanDist, i))
        
        heapElem = minDistance[:]
        heapq.heapify(heapElem)

        for i in range(k):
            val = heapq.heappop(heapElem)
            res.append(points[val[1]])
        
        return res
        
        