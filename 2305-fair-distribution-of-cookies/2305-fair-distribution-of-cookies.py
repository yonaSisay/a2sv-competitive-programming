class Solution:
    def __init__(self):
        self.ans = float('inf')
    
    def backTrack(self, arr, i,k, cookies,maxx):
        if maxx >= self.ans:
            return
        
        if i >= len(cookies):
            self.ans = min(maxx, self.ans)
            return 
              
        
        for j in range(k):
            arr[j] += cookies[i]
            maxx1 = max(arr[j],maxx)
            self.backTrack(arr, i + 1, k, cookies,maxx1)
            arr[j] -= cookies[i]
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse = True)
        self.backTrack(k * [0], 0, k,cookies,0)
        
        return self.ans