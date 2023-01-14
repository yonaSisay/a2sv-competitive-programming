class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        x = king[0]
        y = king[1]
#         to right
        while y!=8:
            y +=1
            if [x,y] in queens:
                ans.append([x,y])
                break
        x = king[0]
        y = king[1]
#           to left
        while y!=-1:
            y -=1
            if [x,y] in queens:
                ans.append([x,y])
                break
        x = king[0]
        y = king[1]
#     to  down
        while x!=8:
            x+=1
            if [x,y] in queens:
                ans.append([x,y])
                break
        x = king[0]
        y = king[1]
#   to top
        while x!=-1:
            x-=1
            if [x,y] in queens:
                ans.append([x,y])
                break
        x = king[0]
        y = king[1]
#                 forward
        while x!=8:
            x +=1
            y +=1
            if [x,y] in queens :
                ans.append([x,y])
                break
        x = king[0]
        y = king[1]
        while x!=-1:
            x -=1
            y -=1
            if [x,y] in queens :
                ans.append([x,y])
                break
        x = king[0]
        y = king[1]
#  reverse
        while x!=8:
            x +=1
            y -=1
            if [x,y] in queens :
                ans.append([x,y])
                break
        x = king[0]
        y = king[1]
        while y!=8:
            x -=1
            y +=1
            if [x,y] in queens :
                ans.append([x,y])
                break
        x = king[0]
        y = king[1]            

        return ans