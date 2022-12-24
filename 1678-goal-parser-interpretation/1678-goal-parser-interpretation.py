class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        n = len(command)
        for i in range(n):
            if command[i] == "G":
                ans += "G"
            elif command[i] == "(" and command[i+1]==")":
                ans += "o"
            elif command[i] == "(" and command[i+1]=="a":
                ans += "al"
        return ans






























