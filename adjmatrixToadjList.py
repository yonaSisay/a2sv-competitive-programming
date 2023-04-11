from collections import defaultdict

adjList = defaultdict(list)

n = int(input())

for i in range(n):
    arr = list(map(int,input().split()))
    
    for j in range(n):
        if arr[j]:
            adjList[i + 1].append(j + 1)
arr = list(adjList.keys())
arr.sort()

for key in arr:
    print(len(adjList[key]), *adjList[key])