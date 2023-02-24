n = int(input())
for i in range(n):
    temp = input()
    temp1 = temp[0:2] +"... "+temp[0:len(temp)]+"?"
    print(temp1)
