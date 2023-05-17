class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = {i: i for i in range(n)}
        size = [1]*n

        def find(x):
            if parent[x] == x:
                return x
            cur = find(parent[x])
            parent[x] = cur
            return cur
        
        def union(x,y):
            parentX = find(x)
            parentY = find(y)
            
            if parentX != parentY:
                if size[parentX] > size[parentY]:
                    parent[parentY] = parentX
                    size[parentX] += size[parentY]
                else:
                    parent[parentX] = parentY
                    size[parentY] += size[parentX]

            
        for x,y in edges:
            union(x,y)
        
        return find(source) == find(destination)