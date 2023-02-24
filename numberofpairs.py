n = int(input())
boy = list(map(int, input().split()))
m = int(input())
girl = list(map(int, input().split()))
 
boy.sort()
girl.sort()
 
left = 0
right = 0
 
count = 0
 
while left < n and right < m:
    temp = abs(boy[left] - girl[right])
 
    if temp <= 1:
        count += 1
        left , right = left + 1, right + 1
    elif temp > 1:
        if boy[left] > girl[right]:
            right += 1
        else:
            left += 1
print(count)
