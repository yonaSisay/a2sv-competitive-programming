class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        arr = [0]*n
        ans = []
        for edge in edges:
            arr[edge[1]] = 1
        
        for i in range(n):
            if not arr[i]:
                ans.append(i)
        
        return ans