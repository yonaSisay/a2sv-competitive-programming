class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        maxx = 0

        def backTrack(arr, idx, count):
            nonlocal maxx

            if idx >= len(requests):
                flag = True
                for num in arr:
                    if num != 0:
                        flag = False
                        break
                if flag:
                    maxx = max(count, maxx)
                return

            arr[requests[idx][0]] += 1
            arr[requests[idx][1]] -= 1          


            backTrack(arr,idx + 1,count + 1)

            arr[requests[idx][0]] -= 1
            arr[requests[idx][1]] += 1

            
            backTrack(arr,idx + 1,count)
        
        backTrack([0]*n, 0, 0)

        return maxx