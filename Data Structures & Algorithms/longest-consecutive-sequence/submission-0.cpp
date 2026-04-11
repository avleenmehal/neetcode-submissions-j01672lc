class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int ans = 0;
        int longest = 0;

        for(int n: numSet) {
            if(numSet.find(n-1)==numSet.end()) {
                longest = 1;
                while(numSet.find(n+longest) != numSet.end()) {
                    longest++;

                }
                ans = max(longest, ans);
            }
        }
        return ans;
    }
};
