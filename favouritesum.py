N  = int(input())


for _ in range(N):
    m,n = list(map(int, input().split()))
    fav = list(map(int, input().split()))
    fav.sort()
    summ = ((1 + n) * n) // 2
    
    for num in fav:
        if num <= n:
            summ -= num*2
    print(summ)