class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l =0;
        int r = heights.size()-1;

        int ans = 0;
        while(l<r) {
            int vol = 0;
            int h = min(heights[l],heights[r]);
            int w = r - l;
            vol = h*w;
            ans = max(ans,vol);
            if(heights[l]< heights[r]){
                l++;
            }else {
                r--;
            }
        }
        return ans;
    }
};
