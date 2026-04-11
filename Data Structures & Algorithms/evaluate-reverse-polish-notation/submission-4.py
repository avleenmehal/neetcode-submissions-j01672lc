class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop()+ stack.pop())
            elif c == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a,b = stack.pop(), stack.pop()
                ans = b // a
                print(ans)
                ans = int(float(b) / a)
                print(ans)
                stack.append(ans)
            else:
                stack.append(int(c))
        return stack[0]