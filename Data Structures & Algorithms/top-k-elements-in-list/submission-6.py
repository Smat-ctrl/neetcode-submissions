class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmapCount = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for i in range(len(nums)):
            hashmapCount[nums[i]] += 1
        
        for key, value in hashmapCount.items():
            freq[value].append(key)
        
        for i in range(len(freq) - 1, 0, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res
        




        

