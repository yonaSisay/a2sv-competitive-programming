class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = {'*',"-","/","+"}
        
        for char in tokens:
            if char in operation:
                temp1 = stack.pop()
                temp2 = stack.pop()
                ans = 0
                if char == "+":
                    ans = temp1 + temp2
                elif char == "*":
                    ans = temp1 * temp2
                elif char == "-":
                    ans = temp2 - temp1
                elif char == "/":
                    ans = temp2 / temp1
                    if ans > 0:
                        ans = math.floor(ans)
                    else:
                        ans = math.ceil(ans)
                stack.append(ans)
            else:
                stack.append(int(char))
        
        return stack[-1]