class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        acc = defaultdict(set)
        rep = [i for i in range(len(accounts))]
        size = [1]*len(accounts)
        for i,account in enumerate(accounts):
            acc[i] = set(account[1::])


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
                else:
                    rep[repy] = repx
                    size[repx] += size[repy]

        for i in range(len(acc)):
            for j in range(i + 1, len(acc)):
                if acc[i] & acc[j]:
                    union(i,j)
        ans = []

        for i in range(len(rep)):
            if i != rep[i]:
                temp = find(rep[i])
                acc[temp] = acc[i].union(acc[temp])
      
        for i in range(len(rep)):
            if i == rep[i]:
                email = acc[i]
                temp = [accounts[i][0]]
                temp.extend(sorted(email))
                ans.append(temp)
        return ans