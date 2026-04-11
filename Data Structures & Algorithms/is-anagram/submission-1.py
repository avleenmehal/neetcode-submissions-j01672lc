class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char1 = defaultdict(int)
        char2 = defaultdict(int)

        if not len(s) == len(t):
            return False
        
        for i in range(len(s)):
            char1[s[i]] += 1
            char2[t[i]] += 1
        
        return char1 == char2