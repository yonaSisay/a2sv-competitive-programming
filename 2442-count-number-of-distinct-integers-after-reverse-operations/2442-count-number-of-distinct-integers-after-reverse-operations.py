class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        arr = []
        for num1 in nums:
            num = num1
            reversed_num = 0
            while num != 0:
                digit = num % 10
                reversed_num = reversed_num * 10 + digit
                num //= 10
            arr.append(reversed_num)
        
        setn = set()
        nums.extend(arr)
        setn.update(nums)
        
        return len(setn)