class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        rep = {(i,j):(i,j) for i in range(n) for j in range(m)}
        size = {(i,j):1 for i in range(n) for j in range(m)}
        
        d = {
            1: set([(0,1),(0,-1,)]),
            2: set([(1,0),(-1,0)]),
            3: set([(0,-1),(1,0)]),
            4: set([(0,1),(1,0)]),
            5: set([(-1,0),(0,-1)]),
            6: set([(-1,0),(0,1)])
        }    

        def inbound(x,y):
            return  0 <= x < n and 0 <= y < m

        def find(x):
            if rep[x] == x:
                return x
 
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x, y):
            xrep = find(x)
            yrep = find(y)
            if xrep == yrep:
                return [x,y]
            if size[xrep] > size[yrep]:
                rep[yrep] = rep[xrep]
                size[xrep]+=size[yrep]
            else:
                rep[xrep] = rep[yrep]
                size[yrep]+=size[xrep]
            return None
            
        
        for i in range(n):
            for j in range(m):
                curr = grid[i][j]
                for x,y in d[curr]:
                    nr = i + x
                    nc = j + y

                    if inbound(nr,nc):
                        new = grid[nr][nc]

                        if (-x,-y) in d[new]:
                            union((nr,nc),(i,j))
        
        return find((0,0)) == find((n - 1,m - 1))