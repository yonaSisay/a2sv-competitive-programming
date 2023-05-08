# 8
# 2
# 2 3
# 3
# 1 2 3
# 4
# 1 2 3 4
# 3
# 0 0 2
# 2
# 6 2
# 3
# 0 0 2
# 5
# 8 2 0 1 1
# 5
# 0 1 0 0 6
import heapq
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    heap = []
    talkes = 0
    ans = []
    
    for i,val in enumerate(arr):
        if val:
            heapq.heappush(heap,(-val, i + 1))
            
    while len(heap) > 1:
        val1,idx1 = heapq.heappop(heap)
        val2,idx2 = heapq.heappop(heap)
        
        talkes += 1
        ans.append((idx1,idx2))
        
        val1, val2 = val1 + 1,val2 + 1
        if val1 < 0:
            heapq.heappush(heap, (val1,idx1)) 
        if val2 < 0:    
            heapq.heappush(heap, (val2,idx2)) 
    
        
    print(talkes) 
    [print(*x) for x in ans]
    
for _ in range(int(input())):
    solve()