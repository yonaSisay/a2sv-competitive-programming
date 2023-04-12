class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = set()

        def dfs(node, arr):
            if not arr:
                arr.append(node)

            if not graph[node] or node == len(graph) - 1:
                if arr and arr[-1] == len(graph) - 1:
                    ans.add(tuple(arr))
                return
           

            for elm in graph[node]:
                arr.append(elm)
                dfs(elm , arr[:])
                arr.pop()
        
        dfs(0,[])

        return ans