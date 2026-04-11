class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     l = 0
    #     r = len(s) - 1

    #     while l<=r :
    #         if s[l] == s[r]:
    #             l += 1
    #             r -= 1
    #             continue
    #         else:
    #             return False
    #     return True
    
     def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        print(newStr)
        return newStr == newStr[::-1]