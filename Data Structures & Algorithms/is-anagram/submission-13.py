class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = defaultdict(int)
        hashmap2 = defaultdict(int)
        if len(s) != len(t):
            return False
        
        for c in s:
            hashmap1[c] += 1
        for c in t:
            hashmap2[c] += 1
        
        for key in hashmap1:
            if hashmap1[key] != hashmap2[key]:
                return False
        
        return True
