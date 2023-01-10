class Solution:
    def printVertically(self, s: str) -> List[str]:
        ls = s.split()
        ans = []
        maxim = max(ls,key=len)
        for i in range(len(maxim)):
            temp = ""
            for j in range(len(ls)):
                if i>= len(ls[j]):
                    temp +=" "
                else:
                    temp += ls[j][i]
            i = len(temp)-1
            while temp[i]==" ":
                temp = temp[:-1]
                i -=1
            ans.append(temp)
        return ans