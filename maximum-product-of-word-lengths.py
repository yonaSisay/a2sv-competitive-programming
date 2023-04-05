class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        bits = []

        for i in range(len(words)):
            temp = [0] * 26
            offset = ord('a')

            for ch in words[i]:
                temp[ord(ch) - offset] = 1
            num = int("".join(map(str, temp)), 2)
            bits.append(num)
        
        for i in range(len(words)):
            for j in range(i, len(words)):
                if  (bits[j] & bits[i]) == 0:
                    ans = max(ans, len(words[i]) * len(words[j]) )
        
        return ans