class Solution:
    def racecar(self, target: int) -> int:
        visited = set([(0,1)])
        queue = deque([(0,1)])
        level = 0


        def helper(position, speed, In):
            if In == "A":
                position += speed
                speed *= 2
            else:
                if speed > 0:
                    speed = -1
                else:
                    speed = 1
            return[position, speed]
                
        while queue:
            for _ in range(len(queue)):
                position, speed = queue.popleft()
                
                if position == target:
                    return level
                
                for ch in ["A","R"]:
                    p,s = helper(position, speed, ch)                 
                    if (p,s) not in visited:
                        queue.append((p,s))
                        visited.add((p,s))
            level += 1