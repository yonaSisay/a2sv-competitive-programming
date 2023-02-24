n = int(input())
temp= list(map(int,input().split())) 
count = 0
lowest = temp[0]
highest = temp[0]
 
for elm in temp:
    if elm > highest:
        count +=1
        highest=elm
    elif elm < lowest:
        count +=1
        lowest = elm
print(count)
