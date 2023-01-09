class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dict_ = {}
        ans = []
        
        for cpdomain in cpdomains:
            temp = cpdomain.split()
            rep = int(temp[0])
            domains = temp[1].split(".")
            n = len(domains)
            if n!=2:
                maindom = domains[1]+"."+domains[2]
                if maindom in dict_:
                    dict_[maindom] +=rep
                else:
                    dict_[maindom] =rep
            if temp[1] not in dict_:
                dict_[temp[1]]=rep
            else:
                dict_[temp[1]]+=rep
            if domains[n-1] in dict_:
                dict_[domains[n-1]]+=rep
            else:
                dict_[domains[n-1]]=rep
        for key,value in dict_.items():
            dom = str(value) + " " + key
            ans.append(dom)
        return ans