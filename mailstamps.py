
from collections import defaultdict
from collections import deque

graph = defaultdict(list)


for _ in range(int(input())):
    arr = list(map(int, input().split()))
    graph[arr[0]].append(arr[1])
    graph[arr[1]].append(arr[0])

tt = [x for x in graph if len(graph[x]) == 1]

queue = deque([tt[0]])
visited = set([tt[0]])
ans = []
while queue:
    node = queue.popleft()
    ans.append(node)
    
    for elm in graph[node]:
        if elm not in visited:
            queue.append(elm)
            visited.add(elm)
print(*ans)