class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
#         to hash maps to compare the number of occurance of the characters
        mapp = Counter(s1)
         
        for i in range(len(s2) - len(s1) + 1):
            if Counter(s2[i:i + len(s1)]) == mapp:
                return True

        return False