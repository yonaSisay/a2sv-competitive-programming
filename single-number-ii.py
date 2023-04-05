class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr = [0] * 32

        negs = 0
        for i in range(len(nums)):
            
            if  nums[i] < 0:
                negs += 1
        
            n = abs(nums[i])

            count = 0

            while n:
                arr[count] += n & 1

                n = n >> 1
                count += 1
        
        
        for i in range(len(arr)):
            arr[i] = arr[i] % 3
        
        if negs % 3 == 0:
            return int("".join(map(str, arr[::-1])), 2)     
        
        return -1 * int("".join(map(str, arr[::-1])), 2)