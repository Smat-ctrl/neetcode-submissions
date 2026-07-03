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
        
        for items in hashmap1:
            if hashmap2[items] == 0:
                return False
            if  hashmap1[items] != hashmap2[items]:
                return False
        
        return True
