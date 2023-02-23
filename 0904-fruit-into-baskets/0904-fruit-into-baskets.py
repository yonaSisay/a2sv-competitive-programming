class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mapp = defaultdict(int)
        maxx = 0
        left = 0
        
        for i in range(len(fruits)):
            mapp[fruits[i]] += 1
            while  len(mapp) > 2:
                mapp[fruits[left]] -= 1
                if mapp[fruits[left]] == 0:
                    del mapp[fruits[left]]
                left += 1  
            maxx = max(sum(mapp.values()) , maxx)
        return maxx
               