class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxx = 0

        def backTrack(idx, chars):
            nonlocal maxx
            if idx >= len(arr):
                return
            flag = True
            mapp = Counter("".join(chars))
            
            if len(set(arr[idx])) != len(arr[idx]):
                flag = False

            for ch in arr[idx]:
                if ch in mapp:
                    flag = False

            if not arr or flag:
                chars.append(arr[idx])
                temp = "".join(chars)
                
                maxx = max(maxx, len(temp))

                backTrack(idx + 1, chars[:])
                chars.pop()

            backTrack(idx + 1, chars[:])
        
        backTrack(0, [])

        return maxx