class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        colors = [0]*numCourses
        for end, source in prerequisites:
            graph[source].append(end)
        
        ans =[]
        def hasCycle(node):
            if colors[node] == 1:
                return False
            
            if colors[node] == 2:
                return True
            
            colors[node] = 1
        
            for elm in graph[node]:
               if not hasCycle(elm):
                  return False
            
            colors[node] = 2
            ans.append(node)
            return True

        for index in range(numCourses):
            if not hasCycle(index):
                return []
        return ans[::-1]