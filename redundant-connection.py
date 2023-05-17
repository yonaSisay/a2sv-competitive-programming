class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i: i for i in range(1, len(edges) + 1)}
        size = [1]*len(edges)

        def find(x):
            if parent[x] == x:
                return x
            
            curr = find(parent[x])
            parent[x] = curr
            return curr
        
        for x,y in edges:
            parX = find(x)
            parY = find(y)

            if parX == parY:
                return [x,y]

            if size[parX - 1] < size[parY - 1]:
                parent[parX] = parY
                size[parY - 1] += size[parX - 1]
            else:
                parent[parY] = parX
                size[parX - 1] += size[parY - 1]