n,m = map(int,input().split())
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
l=0
for num in nums2:
    for i in range(l,n):
        if num<=nums1[i]:
            l=i
            print(l,end = " ")
            break
        
    if num > nums1[n-1] :
        print(n,end = " ")
