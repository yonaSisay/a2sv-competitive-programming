class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mapp = defaultdict(int)
        maxx = left = right = 0
        
        while right < len(fruits) and left < len(fruits):
            if len(mapp) != 3:
                mapp[fruits[right]] += 1
                right += 1
            if len(mapp) == 3:
                mapp[fruits[left]] -= 1
                if mapp[fruits[left]] == 0:
                    del mapp[fruits[left]]
                left += 1
            if len(mapp) <= 2:
                temp = 0
                for num in mapp:
                    temp += mapp[num] 
                maxx = max(temp,maxx)
        return maxx            