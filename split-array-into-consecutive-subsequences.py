class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        H = []
        for n in nums:
            while H:
                val, _len = H[0]
                if n - val == 1:
                    heapreplace(H, (n, _len+1))
                    break
                elif n == val:
                    heappush(H, (n, 1))
                    break
                else:
                    if _len < 3:
                        return False
                    heappop(H)
            else:
                heappush(H, (n, 1))
                
        return all(x > 2 for val, x in H)