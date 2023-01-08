class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = []
        d = defaultdict(list)
        for path in paths:
            temp = path.split()
            # print(temp)
            for i in range(1,len(temp)):
                temp2 = temp[i].split("(")
                # temp2 = re.split('\(|\)',temp[i])
                # print(temp2)
                if temp2[1] in d:
                    d[temp2[1]].append(temp[0]+"/"+temp2[0])
                else:
                    d[temp2[1]].append(temp[0]+"/"+temp2[0])
        for i,j in d.items():
            if len(j)!=1:
                ans.append(j)
        return ans