import heapq
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    whiteboards = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    heapq.heapify(whiteboards)
    
    for num in b:
        temp = heapq.heappop(whiteboards)
        heapq.heappush(whiteboards, num)
    print(sum(whiteboards))