if __name__ == '__main__':
    N = int(input())
    
    arr = []
    for i in range(N):
        temp = input().split()
        if temp[0] == "insert":
            arr.insert(int(temp[1]),int(temp[2]))
        elif temp[0] == "print":
            print(arr)
        elif temp[0] == "remove":
            arr.remove(int(temp[1]))
        elif temp[0] == "append":
            arr.append(int(temp[1]))
        elif temp[0] == "sort":
            arr.sort()
        elif temp[0] == "reverse":
            arr.reverse()
        elif temp[0] == "pop":
            arr.pop()
