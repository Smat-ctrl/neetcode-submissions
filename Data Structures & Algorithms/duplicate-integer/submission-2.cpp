class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> hashMap;

        for (int i = 0; i < nums.size(); ++i) {
            auto it = hashMap.find(nums[i]);
            if (it != hashMap.end() && it->second != i) {
                return true;
            }
            hashMap[nums[i]] = i;
        }
        return false;
    }
};