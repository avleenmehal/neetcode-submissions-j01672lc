class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<int> right(prices.size());
        // for(int i =0;i<prices.size();i++) {
        //     right[n-i]

        // }
        int lowest = prices[0];
        int ans = 0;
        for(int i =1 ;i<prices.size();i++) {
            if(prices[i]> lowest) {
                ans = max(ans, prices[i]-lowest);
            } else{
                lowest = prices[i];
            }
        }
        return ans;
    }
};
