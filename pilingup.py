# Enter your code here. Read input from STDIN. Print output to STDOUT

# on the top mehon sideLength[j] > sideLength[i]
T = int(input())
for i in range(T):
    bsize = int(input()) - 1
    blocks = list(map(int,input().split()))
    temp = float("inf")
    left = 0
    ans = "Yes"
    while(left<bsize):
        if blocks[left]>=blocks[bsize]:
            if blocks[left]>temp:
                print("No")
                ans = "No"
                break
            else:
                temp = blocks[left]
                left += 1
        elif blocks[left]<blocks[bsize]:
            if blocks[bsize]>temp:
                print("No")
                ans = "No"
                break
            else:
                temp = blocks[bsize]
                bsize -= 1
    if ans == "Yes":
        print("Yes")
