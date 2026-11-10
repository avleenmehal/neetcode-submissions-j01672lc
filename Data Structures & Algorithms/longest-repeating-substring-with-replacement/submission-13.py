class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        mp = defaultdict(int) # store the count of characters within the substring l to r  

        maxfreq = 0
        ans = 0
        while (l<=r and l<len(s) and r<len(s)):
            mp[s[r]] += 1
            maxfreq = max(maxfreq,mp[s[r]])

            while ((r-l+1) - maxfreq > k):
                mp[s[l]] -= 1
                l += 1
            
            ans = max(ans, r -l +1)
            r+=1
            
        return ans





        