class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(openused, closeused, s):

            if openused == n and closeused == n:
                res.append(s)
                return

            if openused <n:
                dfs(openused+1, closeused, s+'(')

            if closeused<openused:
                dfs(openused, closeused+1, s+')')

        dfs(0,0,"")


    
        return res