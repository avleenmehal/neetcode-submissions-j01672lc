class Solution {
public:
    string minWindow(string s, string t) {

        if(t.empty()) return "";
        
        unordered_map<char,int> countT;
        unordered_map<char,int> window;

        for(char c: t){
            countT[c]++;
        }

        int have =0; 
        int need = countT.size();

        int reslen = INT_MAX;
        pair<int,int> res = {-1,-1};

        int l=0; int r = 0;
        while(r<s.length()){
            window[s[r]]++;

            if(countT.count(s[r]) && window[s[r]]==countT[s[r]]) {
                have++;
            }

            while(have==need) {
                if(r - l +1 <reslen) {
                    reslen = r-l+1;
                    res={l,r};
                }

                window[s[l]]--;
                if(countT.count(s[l]) && countT[s[l]]>window[s[l]]) {
                    have--;
                }
                l++;
            }
            r++;

        }
        return reslen == INT_MAX ? "" : s.substr(res.first,reslen);
    }
};
