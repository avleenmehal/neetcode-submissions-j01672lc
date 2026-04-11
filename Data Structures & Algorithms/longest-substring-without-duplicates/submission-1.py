class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        mp = set()
        # mp.add(s[l]) 

        for r in range(len(s)):
            while s[r] in mp:
                mp.remove(s[l])
                l += 1
            mp.add(s[r])
            ans = max(ans, r-l+1)
        
        return ans
            

        