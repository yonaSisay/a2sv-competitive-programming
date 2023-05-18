class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rep = [i for i in range(len(stones))]
        size = [1] * len(stones)

        def find(x):
            if x == rep[x]:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x,y):
            parx = find(x)
            pary = find(y)
            if parx != pary:
                if size[parx] < size[pary]:
                    rep[parx] = rep[pary]
                    size[pary] += size[parx]
                else:
                    rep[pary] = rep[parx]
                    size[parx] += size[pary]

        for i in range(len(stones)):
            for j in range(i,len(stones)):
                x,y = stones[i]
                v,z = stones[j]

                if x == v or y == z:
                    union(i,j)
        ans = 0 
        pars = set(rep)
        for key,val in enumerate(rep):
            if key == val:
                ans += size[val] - 1
        return ans