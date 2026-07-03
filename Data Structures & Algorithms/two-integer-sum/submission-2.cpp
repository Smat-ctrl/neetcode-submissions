class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int>hashMap;

        for (int i = 0; i < nums.size(); i++) {
             hashMap[nums[i]] = i;
            }

        for (int i = 0; i < nums.size(); ++i) {
            int key = target - nums[i];
            auto it = hashMap.find(key);
            if (it != hashMap.end() && it->second != i) {
                return {i, it->second};
            }
        }
        return {0,0};
    }
};
