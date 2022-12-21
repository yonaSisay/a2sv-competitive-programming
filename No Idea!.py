def beHappy():
    num= input()
    nums = input().split(" ")
    nums2 = set(input().split(" "))
    nums3 = set(input().split(" "))
    c = 0
    for x in nums:
        if x in nums2:
            c+=1
        elif x in nums3:
            c-=1
    print(c)
beHappy()
        
