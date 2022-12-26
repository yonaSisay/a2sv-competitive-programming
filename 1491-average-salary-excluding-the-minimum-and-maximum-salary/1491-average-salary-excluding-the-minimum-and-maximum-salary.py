class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        average = 0
        for i in range(1,len(salary)-1):
            average += salary[i]
        n=len(salary)-2
        average = average/n
        return average