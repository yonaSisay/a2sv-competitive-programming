# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
nums = input().split(" ") 
n = int(nums[0])
m = int(nums[1])
group_a = defaultdict(list)
ans = []
for i in range(1,n+1):
    group_a[input()].append(i)
for i in range(m):
    temp = input()
    if temp in group_a:
        print(*group_a[temp])
    else:
        print(-1)
