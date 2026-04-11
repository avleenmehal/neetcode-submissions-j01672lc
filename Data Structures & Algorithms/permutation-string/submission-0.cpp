class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if(s1.length() > s2.length()) 
        return false;

        vector<int> arr1(26,0);
        vector<int> arr2(26,0);
        for(int i =0;i<s1.length();i++) {
            arr1[s1[i]-'a']++;
            arr2[s2[i]-'a']++;
        }
        int matches =0;
        for(int i=0;i<26;i++){
            if(arr1[i] == arr2[i]) 
            {
                matches++;
            }
        }
        int l=0;int r=s1.length();
        while(r<s2.length()) {
            if(matches == 26)
            return true;

            int index = s2[l]-'a';
            arr2[index]--;
            if(arr1[index]==arr2[index]) {
                matches++;
            } else if(arr1[index]==arr2[index]+1) {
                matches--;
            }
            l++;

            index = s2[r]-'a';
            arr2[index]++;
            if(arr1[index]==arr2[index]) {
                matches++;
            } else if(arr1[index]==arr2[index]-1) {
                matches--;
            }
            r++;
        }
        if(matches==26){
            return true;
        }
        return false;
    }
};
