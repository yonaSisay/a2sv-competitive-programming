class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0]*len(graph)
        ans = []

        def hasCycle(index):
            if color[index] == 1:
                return False
            
            if color[index] == 2:
                return True
            
            color[index] = 1

            for elm in graph[index]:
                if not hasCycle(elm):
                    return False

            color[index] = 2
            ans.append(index)
            
            return True
        
        for i in range(len(graph)):
            hasCycle(i)

        ans.sort()
        return ans