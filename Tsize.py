N = int(input())
for i in range(N):
    temp =input().split()
    l1 = len(temp[0])
    l2 = len(temp[1])
    if temp[0][l1-1]==temp[1][l2-1] and temp[0][l1-1]=="S":
        if l1>l2:
            print("<")
        elif l1<l2:
            print(">")
        else:
            print("=")
    elif temp[0][l1-1]==temp[1][l2-1] and temp[0][l1-1]=="L":
        if l1>l2:
            print(">")
        elif l1<l2:
            print("<")
        else:
            print("=")
    elif temp[0][l1-1]=="L" and temp[1][l2-1]=="M":
        print(">")
    elif temp[1][l2-1]=="L" and temp[0][l1-1]=="M":
        print("<")
    elif temp[0][l1-1]=="L" and temp[1][l2-1]=="S":
        print(">")
    elif temp[1][l2-1]=="L" and temp[0][l1-1]=="S":
        print("<")
    elif temp[0][l1-1]=="M" and temp[1][l2-1]=="S":
        print(">")
    elif temp[1][l2-1]=="M" and temp[0][l1-1]=="S":
        print("<")
    elif temp[0][l1-1]==temp[1][l2-1] and temp[0][l1-1]=="M":
        print("=")
    
