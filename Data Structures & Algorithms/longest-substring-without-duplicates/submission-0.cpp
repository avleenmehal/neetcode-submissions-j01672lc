class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.size()==0) return 0;
        unordered_set<char> set;
        int longest = 1;
        // set.insert(s[0]);
        int i =0;
        int j =0;
        while(j < s.size())
        {
            int temp = 0;
            while(set.find(s[j]) != set.end()) {
                
                set.erase(s[i]);
                i++;
            }

            set.insert(s[j]);
            longest = max (longest, j-i+1);
            j++;
        }
        return longest;
    }
};
