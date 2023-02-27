class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        changes = [0] * (len(s) + 1)
        ans = ""        
        for shift in shifts:
            if shift[2] == 0:
                changes[shift[0]] -= 1
                changes[shift[1] + 1] += 1
            else:
                changes[shift[0]] += 1
                changes[shift[1] + 1] -= 1
        
        prefix = list(accumulate(changes))
        
        for i in range(len(s)):
            ans += chr(97 + ((ord(s[i]) + prefix[i]) - 97) % 26)
        return ans