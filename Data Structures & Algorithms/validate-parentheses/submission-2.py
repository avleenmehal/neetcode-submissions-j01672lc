class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            print(stack)
            if c == '}':
                if not stack or stack[-1] != '{':
                    return False
                else:
                    print("here")
                    stack.pop()
            elif c ==']':
                if not stack or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            elif c==')':
                if not stack or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return True if not stack else False
        