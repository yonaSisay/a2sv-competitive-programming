
n = int(input())
count = 0
for _ in range(n):
    arr = list(map(int,input().split()))
    for i in range(n):
        if arr[i]:
            count += 1
print(count // 2)