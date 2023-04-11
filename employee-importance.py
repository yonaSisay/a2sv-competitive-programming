"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adjList = defaultdict(list)
        
        for emp in employees:
            adjList[emp.id].append(emp.importance)
            adjList[emp.id].append(emp.subordinates)
        print(adjList)
    
        def dfs(id):
                if not adjList[id][1]:
                    return adjList[id][0]
                current = adjList[id][0]
                
                summ = 0

                for num in adjList[id][1]:
                    summ += dfs(num)
                return summ + current

        return dfs(id)