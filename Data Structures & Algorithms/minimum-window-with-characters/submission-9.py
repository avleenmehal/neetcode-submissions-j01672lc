class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        ans = ""
        
        def checkAllPresent(s1,t1):
            for k,v in t1.items():
                if s1.get(k,0) < v:
                    return False
            print("returning teu")
            print(s1)
            return True

            
        count = defaultdict(int)
        for i in range(len(t)):
            count[t[i]] += 1
        
        countBig = defaultdict(int)

        l=0
        r=0
        start = 0
        end = len(s)
        minLen = float("inf")

        while r<len(s):
            countBig[s[r]]+=1 
            while checkAllPresent(countBig, count):
                if minLen > r-l+1:
                    minLen = r-l+1
                    start = l
                    end = r
                countBig[s[l]]-=1
                l+=1
                
                # while checkAllPresent(countBig, count):
                #     countBig[s[l]] -=1
                #     l+=1

            r+=1
        print(minLen)
        ans = s[start:end+1] if minLen != float("inf") else ""

        return ans