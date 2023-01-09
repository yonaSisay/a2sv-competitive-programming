class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for i in range(len(boxes)):
            sum = 0
            for j in range(len(boxes)):
                if boxes[j]=='1' and i!=j:
                    temp = abs(i-j)
                    sum += temp
            ans.append(sum)
        return ans