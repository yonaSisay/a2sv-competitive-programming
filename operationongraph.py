from collections import defaultdict

n = int(input())
op = int(input())

adjList = defaultdict(list)

for i in range(op):
    temp = list(map(int,input().split()))
    if temp[0] == 1:
        adjList[temp[1]].append(temp[2])
        adjList[temp[2]].append(temp[1])
    else:
        print(*adjList[temp[1]])