class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # arr = [0]*n
        # for i in range(n):
        #     for j in range(n):
        #         if nums[i]>nums[j]:
        #             arr[i]+=1
        temp = sorted(nums)
        mapp = {}
        result=[]
        for i in range(len(temp)):
            if temp[i] not in mapp:
                mapp[temp[i]]=i
        for i in range(len(nums)):
            result.append(mapp[nums[i]])
        return result