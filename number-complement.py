class Solution:
    def findComplement(self, num: int) -> int:
        length = int.bit_length(num)

        return num ^ ((1 << (length)) - 1)