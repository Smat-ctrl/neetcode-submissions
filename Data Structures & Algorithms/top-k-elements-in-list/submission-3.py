class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)

        for i in range(len(nums)):
            hashMap[nums[i]] += 1
        
        sorted_hash = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)

        return [items[0] for items in sorted_hash[:k]]