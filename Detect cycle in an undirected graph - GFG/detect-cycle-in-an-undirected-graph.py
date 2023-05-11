from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    colors = [0]*V
	    
	    def dfs(node, parent):
            if colors[node] == 1:
                return False
	       
            if colors[node] == 2:
               return True
            
            colors[node] = 1
            
            for elm in adj[node]:
               if elm != parent:
                   if not dfs(elm, node):
                       return False
            colors[node] = 2
            
            return True
	   
        for i in range(v):
           if not dfs(i, V):
               return True
        
        return False

		
             

#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends