n,m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
l = 0
r = 0
ans = []
while r <m and l<n:
    if arr1[l]<arr2[r]:
        ans.append(arr1[l])
        l +=1
    elif arr1[l]>=arr2[r]:
        ans.append(arr2[r])
        r += 1
ans.extend(arr1[l:])
ans.extend(arr2[r:])
print(*ans)
