class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mapp = defaultdict(int)

        for bill in bills:
            if bill == 20:
                if mapp[10] and mapp[5]:
                    mapp[5] -= 1
                    mapp[10] -= 1
                elif not mapp[10] and mapp[5] >= 3:
                    mapp[5] -= 3
                else:
                    return False
            elif bill == 10:
                if mapp[5]:
                    mapp[5] -= 1
                    mapp[10] += 1
                else:
                    return False
            else:
                mapp[5] += 1
        return True