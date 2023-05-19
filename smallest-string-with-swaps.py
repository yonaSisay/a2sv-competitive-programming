class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        rep = [i for i in range(len(s))]
        size = [1]*len(s)
        mapp = {i : [ch] for i,ch in enumerate(s)}
        ans = [""]*len(s)

        def find(x):
            if x == rep[x]:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x,y):
            repx = find(x)
            repy = find(y)

            if repx != repy:
                if size[repx] < size[repy]:
                    rep[repx] = repy
                    size[repy] += size[repx]
                    mapp[repy].extend(mapp[repx])
                else:
                    rep[repy] = repx
                    size[repx] += size[repy]
                    mapp[repx].extend(mapp[repy])
        
        for x,y in pairs:
            union(x,y)

        for key in mapp:
            mapp[key].sort(reverse = True)

        for i in range(len(s)):
            repp = find(i)
            ans[i] = mapp[repp][-1]
            mapp[repp].pop()
         
        return "".join(ans)