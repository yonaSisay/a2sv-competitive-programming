class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if  ch.isalpha() or ch == "[":
                stack.append(ch)
            elif ch.isdigit():
                temp = ch
                if stack and stack[-1].isdigit():
                    temp = stack.pop() + ch
                stack.append(temp)
            else:
                temp = []
                while stack[-1] != "[":
                    temp.append(stack.pop())
                stack.pop()
                temp = temp * int(stack.pop())

                stack.extend(temp[::-1])
        return "".join(stack)