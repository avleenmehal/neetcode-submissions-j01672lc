class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1,-1,-1):
            print(i)
            for word in wordDict:
                if s.startswith(word,i):
                    dp[i]= dp[i+len(word)]
                if dp[i]:
                    break
                print(dp)

        return dp[0]
            
        # def util(s, wordDict, i):
        #     if i == len(s):
        #         return True

        #     for word in wordDict:
        #         j = len(word)

        #         if ((i+j) <= len(s)) and word == s[i:j+i]:
        #             # i = j+i # DONT DO THIS becuase in backtracking we are already updating i
        #             if util(s,wordDict,i+j):
        #                 return True
        #     return False
        
        # return util(s,wordDict,0)