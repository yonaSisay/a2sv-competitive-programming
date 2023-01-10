class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaced = ""
        p = 0
        for i in range(len(s)):
            if p <len(spaces) and i == spaces[p]:
                spaced += " "
                p += 1
            spaced += s[i]
        
        return spaced