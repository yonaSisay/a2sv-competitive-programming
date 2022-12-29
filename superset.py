# Enter your code here. Read input from STDIN. Print output to STDOUT
set_a = set(map(lambda a: int(a),input().split(" ")))
n = int(input())
ans  = True
for i in range(n):
    temp = set(map(lambda a: int(a),input().split(" ")))
    if set_a.issuperset(temp) == False:
        ans = False
print (ans)     
    
