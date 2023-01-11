class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
#         [2,-1,3,4],
#          [[1,0],[-3,1],[-4,0],[2,3]]
        ans = []
        d = {}  
        sum = 0
        for key,value in enumerate(nums):
            if value%2==0:
                sum += value
            d[key]=value
                    
        for query in queries:
            nums[query[1]]+=query[0]
            if d[query[1]]%2!=0 and nums[query[1]]%2==0:
                sum += nums[query[1]]
                d[query[1]] = nums[query[1]]
                ans.append(sum)
            elif  d[query[1]]%2==0 and nums[query[1]]%2==0:
                sum += query[0]
                d[query[1]] = nums[query[1]]
                ans.append(sum) 
            elif nums[query[1]]%2!=0 and  d[query[1]]%2==0:
                sum -=  d[query[1]]
                d[query[1]] = nums[query[1]]
                ans.append(sum)
            else:
                d[query[1]] = nums[query[1]]
                ans.append(sum) 
        return ans