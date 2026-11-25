class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []

        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        
        heap = [(-freq, val) for val, freq in hashmap.items()]
        heapq.heapify(heap)
        
        for i in range(k):
            freq, val = heapq.heappop(heap)
            res.append(val)
        
        return res
