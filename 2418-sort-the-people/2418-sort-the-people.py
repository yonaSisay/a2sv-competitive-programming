class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(heights)-1,-1,-1):
            mini = i
            for j in range(i,-1,-1):
                if heights[mini] > heights[j]:
                    mini = j
            heights[i],heights[mini]=heights[mini],heights[i]
            names[i],names[mini]=names[mini],names[i]
        
        return names