class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque()
        visited.add(0)
        queue.append(0)

        while queue:
            idx = queue.popleft()

            for i in rooms[idx]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
        
        if len(visited) == len(rooms):
            return True
        return False