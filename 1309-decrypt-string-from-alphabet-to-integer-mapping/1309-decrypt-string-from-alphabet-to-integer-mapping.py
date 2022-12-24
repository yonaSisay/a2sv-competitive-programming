class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz" 
        stack = []
        decrypt=""
        code=""
        
        for char in s:
            if char != "#":
                stack.append(char)
            else:
                index = stack.pop(-2) + stack.pop()               
                code += alphabet[int(index)-1]
                while stack:
                    code+= alphabet[int(stack[-1])-1]
                    stack.pop()
                code = code[::-1]
                decrypt +=code
                code =""
                
        if stack:
            while stack:
                    code+= alphabet[int(stack[-1])-1]
                    stack.pop()
            code = code[::-1]
            decrypt +=code
        
        return decrypt
    