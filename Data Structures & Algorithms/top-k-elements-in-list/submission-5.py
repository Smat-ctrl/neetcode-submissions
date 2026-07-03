class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        res = []
        for i in range(len(nums)):
            freqMap[nums[i]] += 1
        
        for items in freqMap:
            val = (freqMap[items], items)
            res.append(val)
        
        res.sort()

        ans = []
        for j in range(len(res) - 1, len(res) - k - 1, -1):
            ans.append(res[j][1])
        
        return ans
