class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        vertices = [[0,1],[1,0],[-1,0],[0,-1]]
        rowlen = len(image)
        collen = len(image[0])
        visited = set()
        orginal = image[sr][sc]

        def inbound (row,col):
            return 0 <= row < rowlen and 0 <= col < collen
        
        def dfs(sr,sc):
            nonlocal orginal
            nonlocal color

            if not inbound(sr,sc): return

            if image[sr][sc] != orginal:
                return
         
            if (sr,sc) in visited:
                return

            visited.add((sr,sc))
            
            image[sr][sc] = color

            for vertice in vertices:
                nr = sr + vertice[0]
                nc = sc + vertice[1]

                dfs(nr,nc)

        dfs(sr,sc)

        return image