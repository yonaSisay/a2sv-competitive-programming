from collections import deque

def solve():
    arr = []
    n = int(input())
    for _ in range(2):
        temp = input()
        a = []
        for t in temp:
            a.append(int(t))
            
        arr.append(a)
        
    arr.append(temp)
  
    directions = [(0,1),(1,0),(-1,0),(0,-1),(-1,1),(1,-1),(1,1),(-1,-1)]
    
    inbound = lambda x,y: 0 <= x < 2 and 0 <= y < n
    flag = "NO"
    
    queue = deque([(0,0)])
    
    while queue:
        row,col = queue.popleft()
        
        if (row, col) == (1, n - 1):
            return "YES"
        
        for x,y in directions:
            nr, nc = row + x, col + y
            
            if inbound(nr,nc) and not arr[nr][nc]:
                queue.append((nr,nc))
                arr[nr][nc] = 1
        
    
    return "NO"
for _ in range(int(input())):
    print(solve())