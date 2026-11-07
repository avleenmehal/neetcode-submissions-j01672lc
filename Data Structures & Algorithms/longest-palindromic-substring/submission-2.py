class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        startIndex = 0
        length = 0
        dp = [ [False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if ( s[i] == s[j] and (j-i<=2 or dp[i+1][j-1])):
                    dp[i][j] = True
                    if length < j-i+1:
                        startIndex = i
                        length = (j-i + 1)
        # for i in range(n):
        #     print(dp[i])

        return s[startIndex:startIndex+length]
