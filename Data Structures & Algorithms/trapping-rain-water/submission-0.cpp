// class Solution {
// public:
//     int trap(vector<int>& height) {
//         vector<int> leftArr(height.size());
//         int n = height.size();
//         leftArr[0] = height[0];
        
//         vector<int> rightArr(n); 
//         rightArr[n-1] = height[n-1];

//         for(int i = 1; i<n;i++) {
//             leftArr[i] = max(leftArr[i-1], height[i]);
//             rightArr[n-i-1] = max(rightArr[n-i], height[n-i-1]);

            
//         }

//         for(int i = 0; i<n;i++) {
//             cout<< leftArr[i];
//         }
//         cout<<"\n";
//         for(int i = 0; i<n;i++) {
//             cout<< rightArr[i];
//         }
//         cout<<"\n";
//         int area = 0;

//         for(int i = 0 ; i<n;i++) {
//             area += min(leftArr[i],rightArr[i]) - height[i];
//         }
//         return area;
//     }
// };

class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if (n == 0) {
            return 0;
        }

        vector<int> leftMax(n);
        vector<int> rightMax(n);

        leftMax[0] = height[0];
        for (int i = 1; i < n; i++) {
            leftMax[i] = max(leftMax[i - 1], height[i]);
        }

        rightMax[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            rightMax[i] = max(rightMax[i + 1], height[i]);
        }

        for(int i = 0; i<n;i++) {
            cout<< leftMax[i];
        }
        cout<<"\n";
        for(int i = 0; i<n;i++) {
            cout<< rightMax[i];
        }
        cout<<"\n";

        int res = 0;
        for (int i = 1; i < n-1; i++) {
            int added = min(leftMax[i-1], rightMax[i+1]) - height[i];
            cout<<"Added "<< added<< "\n";
            if(added>0) {
                res += added;
            }
            
        }
        return res;
    }
};
