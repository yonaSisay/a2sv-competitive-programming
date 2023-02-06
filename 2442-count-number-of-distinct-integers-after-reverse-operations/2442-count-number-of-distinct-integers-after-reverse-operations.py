class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        arr = []
        for num1 in nums:
            num1 = str(num1)
            v = num1[::-1]
            arr.append(int(v))
            
        setn = set()
        nums.extend(arr)
        setn.update(nums)
        
        return len(setn)