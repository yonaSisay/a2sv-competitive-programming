class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        currentIndex=-1
        value = float("inf")
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                distance = abs(points[i][0]-x)+abs(points[i][1]-y)
                if value > distance:
                    value = distance
                    currentIndex = i
                elif value == distance and currentIndex >i:
                    currentIndex = i
        return currentIndex
                    
                