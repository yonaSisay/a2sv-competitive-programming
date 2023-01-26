class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sum_ = sum(skill)
        no_group = len(skill)/2
        sum_per = sum_/no_group
        skill.sort()
        l = 0
        r = len(skill)-1
        
        ans = 0
        while l < r:   
            if sum_per != skill[l] + skill[r]:
                return -1
            
            ans += skill[l]*skill[r]
            r -= 1
            l += 1
        return ans
            