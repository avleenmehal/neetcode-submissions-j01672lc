class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        if length > len(s2):
            return False
        
        cnt = [0] * 26
        cnt2 = [0] * 26
        
        for i in range(length):
            cnt[ord(s1[i]) - ord('a')] += 1
            cnt2[ord(s2[i]) - ord('a')] += 1

        print(cnt)
        print(cnt2)
        if cnt2== cnt:
            return True
        r = length 
        l =0
        while r < len(s2):
            # if cnt2 == cnt:
            #     return True
            cnt2[ord(s2[r]) - ord('a')] += 1
            cnt2[ord(s2[l]) - ord('a')] -= 1
            if cnt2 == cnt:
                return True
            l += 1
            r += 1

            # print(cnt)
            # print(cnt2)
        
        return False

        
        
        