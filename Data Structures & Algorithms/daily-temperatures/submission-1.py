class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        # for i,t in enumerate(temperatures):
        #     while stack and t > stack[-1][0]:
        #         stackTemp, stackIndex = stack.pop()
        #         res[stackIndex] = i - stackIndex
        #     stack.append((t,i))
        #     print(stack)
        #     print("res")
        #     print(res)

        # return res
        n = len(temperatures)
        for i in range(n-1,-1,-1):
            while stack:
                if stack[-1][0]> temperatures[i]:
                    res[i]=stack[-1][1]-i
                    break
                else:
                    stack.pop()
            stack.append((temperatures[i],i))
        return res
            
        