class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        str1 ={}
        str2 ={}
        for i in s:
            if i in str1:
                str1[i] += 1
            else:
                str1[i] = 1
        print (str1)
        
        for i in t:
            if i in str2:
                str2[i] += 1
            else:
                str2[i] = 1
        print (str2)
        
        for i in str2.keys():
            if i in str1.keys() and str2[i] == str1[i]:
                pass
            else:
                return i
        
