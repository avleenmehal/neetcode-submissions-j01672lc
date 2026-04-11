

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> umap;
        for(int i=0;i<nums.size();i++) {
            if(umap.find(nums[i]) == umap.end()){
                umap.insert(make_pair(nums[i], 1));
            } else return true;
        }
        return false;

    }
};
