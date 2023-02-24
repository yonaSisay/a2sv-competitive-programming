inp = list(map(int, input().split()))
 
temp = inp[0]+inp[1]+(inp[2]*2)
a=inp[0]
b=inp[1]
c=inp[2]
if a>b+1:
    print(b+b+1+c*2)
elif a+1<b:
    print(a+a+1+c*2)
else:
    print(temp)
