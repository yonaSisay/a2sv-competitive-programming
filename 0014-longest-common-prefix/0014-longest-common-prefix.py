class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        sort_str = sorted(strs);
        str1 = sort_str[0]
        str2 = sort_str[len(strs)-1]
       
        for i in range(len(str1)):
            if i > len(str2):
                break
            if str1[i] == str2[i]:
                prefix += str1[i]
            else:
                break
        return prefix