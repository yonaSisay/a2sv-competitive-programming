from collections import defaultdict
from collections import deque

def solve():
    n,m = list(map(int, input().split()))
    golds = list(map(int, input().split()))
    graph = defaultdict(list)
    ans = 0
    
    for _ in range(m):
        temp = list(map(int, input().split()))
        graph[temp[0]].append(temp[1])
        graph[temp[1]].append(temp[0])
    
    bribed = set()
    def bfs(key):
        nonlocal ans
        que = deque([key])
        val = float('inf')
        while que:
            temp = que.popleft()

            val = min(golds[temp - 1], val)

            for elm in graph[temp]:
                if elm not in bribed:
                    que.append(elm)
                    bribed.add(elm)
        ans += val
    
    for i in range(1 , n + 1):
        if i in graph:
            if i not in bribed:
                bribed.add(i)
                bfs(i)
        else:
            ans += golds[i-1]
    
    return ans

print(solve())