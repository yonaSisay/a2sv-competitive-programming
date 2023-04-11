n = int(input())
sinks = [0]*n
source = [0]*n

grid = []

for i in range(n):
    arr = list(map(int, input().split()))
    grid.append(arr)

for i in range(n):
    for j in range(n):
        if grid[i][j]:
            sinks[i] = 1
            source[j] = 1
so = []
si = []
for i in range(n):
    if not sinks[i]:
        si.append(i + 1)
    if not source[i]:
        so.append(i + 1)
        
print(len(so), *so)
print(len(si), *si)