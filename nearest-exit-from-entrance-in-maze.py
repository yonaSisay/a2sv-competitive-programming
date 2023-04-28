class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set([tuple(entrance)])
        queue = deque([tuple(entrance)])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        inbound = lambda x,y: 0 <= x < len(maze) and 0 <= y < len(maze[0])
        level = 0

        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                if maze[r][c] == "." and [r,c] != entrance:
                    for x,y in directions:
                        if not inbound(r + x, c + y):
                            return level
                    
                
                for x,y in directions:
                    nr = r + x
                    nc = c + y

                    if  maze[r][c] == "." and inbound(nr,nc) and (nr,nc) not in visited:
                        visited.add((nr,nc)) 
                        queue.append((nr,nc))
            
            level += 1

        return -1