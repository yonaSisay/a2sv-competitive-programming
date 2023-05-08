n,m,k = list(map(int, input().split()))
arr = []
for _ in range(m + 1):
    arr.append(int(input()))

ans = 0

for i in range(m):
    count = 0
    temp = arr[i]
    fedor = arr[-1]
    
    while fedor or temp:
        
        a = temp & 1
        b = fedor & 1
        
        if a != b:
            count += 1
        
        temp >>= 1
        fedor >>= 1
        
    if count <= k:
        ans += 1

print(ans)
            