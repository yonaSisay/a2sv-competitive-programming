# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
rooms = list(map(int,input().split()))
nums = {}
for elm in rooms:
    if elm in nums:
        nums[elm] +=1
    else:
        nums[elm] = 1
for elm in nums:
    if nums[elm]==1:
        print(elm)
