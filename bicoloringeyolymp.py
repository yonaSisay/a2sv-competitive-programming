from collections import defaultdict
    
def func():
        
    nodes = int(input())
    edges = int(input())
    adjList = defaultdict(list)
    
    for _ in range(edges):
        a,b = map(int, input().split())
        adjList[a].append(b)
        adjList[b].append(a)
    
    color = [-1] * nodes
    visited = set()
    flag = "BICOLOURABLE."
    
    def dfs(node):
        nonlocal flag
        visited.add(node)
        # print(color[node - 1])
        for child in adjList[node]:
            if color[child - 1] != -1:
                if color[child - 1] == color[node - 1]:
                    flag = "NOT BICOLOURABLE."
            else:
                color[child - 1] = int(not color[node - 1] )
            if child not in visited:
                dfs(child)
    color[0] = 0
    dfs(1)
    
    print(flag)
    input()

func()