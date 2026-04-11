class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        l = 0
        r = 0 
        count = defaultdict(int)
        maxf = 0

        while (l<=r and r < len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])

            while ((r-l+1) - maxf > k):
                count[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
            r += 1

        return ans
        