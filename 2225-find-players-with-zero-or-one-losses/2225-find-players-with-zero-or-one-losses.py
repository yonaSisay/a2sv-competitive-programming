class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winLose = {}
        answer = [[],[]]
        for i in matches:
            if i[0] not in winLose:
                winLose[i[0]]= 0
            if i[1] not in winLose:
                winLose[i[1]] = 1
            elif i[1] in winLose:
                winLose[i[1]] +=1
        for i in winLose:
            if winLose[i]==0:
                answer[0].append(i)
            elif winLose[i]==1:
                answer[1].append(i)
        answer[0].sort()
        answer[1].sort()
        return answer