class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def backTrack(arr,idx):
            nonlocal ans

            if idx == len(s) and len(arr) == 4:
                ans.append(".".join(arr))
                return
            
            
            for i in range(idx,len(s)):
                temp = s[idx:i + 1]

                if len(temp) > 1 and temp[0] == "0":
                    return
                
                if int(temp) <= 255 and int(temp) >= 0:
                    arr.append(temp)
                    backTrack(arr,i + 1)
                    arr.pop()
                
        
        backTrack([], 0)

        return ans