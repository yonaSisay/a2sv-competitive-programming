def graph():
    from collections import defaultdict
    
    graph = defaultdict(list)
    
    for _ in range(int(input())):
        arr = list(input().lower().split())
        graph[arr[2]].append(arr[0])
    
    visited = set()
    maxx = 0
    
    def dfs(node ,depth):
        nonlocal maxx
        visited.add(node)
        
        for elm in graph[node]:
            if elm not in visited:
                depth += 1
                dfs(elm, depth)
                depth -= 1
        maxx = max(maxx, depth)
        
    
    dfs("polycarp", 1)
    
    print(maxx)

graph()