class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> number_s(256, 0);
        vector<int> number_t(256, 0);


        for ( char e : s) {
            number_s[e] = number_s[e] + 1;
        }
        for (char e : t) {
            number_t[e] = number_t[e] + 1;
        }
        for (char c = 'a'; c <= 'z'; c++) {
            if (number_s[c] != number_t[c]) {
                return false;
            }
        }
        for (char c = 'A'; c <= 'Z'; c++) {
            if (number_s[c] != number_t[c]) {
                return false;
            }
        }
        return true;
    }
};
