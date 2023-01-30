n = int(input())
arr = list(map(int,input().split()))
left = 0
right = n-1
wube = 0
henock = 0
flag = True

while left<=right:
    if flag:
        if arr[left]>arr[right]:
            wube += arr[left]
            left += 1
        else:
            wube += arr[right]
            right -= 1
        flag = False
    elif not flag:
        if arr[left]>arr[right]:
            henock += arr[left]
            left += 1
        else:
            henock += arr[right]
            right -= 1
        flag = True
print(wube,henock)
