class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = [0]
        ans = 0
        for ch in s:
            if ch == "(":
                stack.append(0)
            elif ch == ")":
                temp = max(1, 2 * stack.pop())
                stack[-1] += temp
        return stack[-1]