class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for elm in edges:
            adjList[elm[0]].append(elm[1])
            adjList[elm[1]].append(elm[0])
        
        for key in adjList:
            if len(adjList[key]) == len(edges):
               return key