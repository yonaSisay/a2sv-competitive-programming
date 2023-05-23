class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        rep = [i for i in range(n)]
        size = [1]*n
        ans = []
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
        
        for x,y in requests:
            repx = find(x)
            repy = find(y)
            flag = True

            for rx,ry in restrictions:
                prx = find(rx)
                pry = find(ry)

                if prx == repx and pry == repy or  pry == repx and prx == repy:
                    flag = False
                    break
            
            if flag: 
                ans.append(True)
                union(x,y)
            else:
                ans.append(False)

        return ans