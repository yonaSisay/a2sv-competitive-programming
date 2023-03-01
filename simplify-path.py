class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
              
        for ch in path:
            if  ch == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            elif ch == "." or ch == "":
                continue
            else:
                stack.append("/" + ch)
        if stack:
            return ''.join(stack)
        return "/"