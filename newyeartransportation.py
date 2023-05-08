n,m = list(map(int , input().split()))
arr = list(map(int, input().split()))
 
indx = 1
flag = False


while indx <= m:
    if indx == m:
        flag = True
        break
    indx = arr[indx - 1] + indx 
 
if flag:
    print("YES")
else:
    print("NO")
    