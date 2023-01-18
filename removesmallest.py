N = int(input())
for i in range(N):
    n= int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    flag = True
    for i in range(n-1):
        diff = abs(nums[i]-nums[i+1])
        if diff>=2:
            flag = False
            print("NO")
            break
        flag = True
    if flag:
        print("YES")
