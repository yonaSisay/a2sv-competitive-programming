class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rep = [i for i in range(n)]
        size = [1]*n
        minn = float('inf')
        def find(x):
            if rep[x] == x:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x,y):
            parx = find(x)
            pary = find(y)

            if parx != pary:
                if size[parx] < size[pary]:
                    rep[parx] = pary
                    size[pary] += size[parx]
                else:
                    rep[pary] = parx
                    size[parx] += size[pary]
        
        for x,y,d in roads:
            union(x - 1,y - 1)
        
        for x,y,d in roads:
            if find(x - 1) == find(0):
                minn = min(minn,d)
        
        return minn