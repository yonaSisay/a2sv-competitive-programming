class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = defaultdict(int)        
        for i in range(len(nums)):
            mapp[nums[i]] = i      
        for i in range(len(nums)):
            if target - nums[i] in mapp and mapp[target - nums[i]] != i :
                return [mapp[target - nums[i]] , i]