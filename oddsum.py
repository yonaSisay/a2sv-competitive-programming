n = int(input())
nums = list(map(int, input().split()))
 
nums.sort()
 
left = 0
right = len(nums) - 1
 
rsum = 0
lsum = 0
 
while left < right:
    lsum += nums[left]
    left += 1
    rsum += nums[right]
    right -= 1
if lsum != rsum:
    print(*nums)
else:
    print(-1)
 
