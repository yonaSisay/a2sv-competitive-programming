from collections import defaultdict
N = int(input())
for i in range(N):
    forwared = defaultdict(int)
    reverse = defaultdict(int)
    m,n= map(int,input().split())
    nums = []
    ans = 0
    for i in range(m):
        temp = list(map(int,input().split()))
        nums.append(temp)
    for i in range(m):
        for j in range(n):
            temp =  i-j
            temp2 = i+j
            forwared[temp]+=nums[i][j]
            reverse[temp2]+=nums[i][j]
    for i in range(m):
        for j in range(n):
            sum = forwared[i-j]+reverse[i+j]-nums[i][j]
            ans = max(ans,sum)
    print(ans)
        
