class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        mapp = defaultdict(int)
        ans = []
        for elm in words[0]:
            mapp[elm] += 1

        for i in range(1,len(words)):
            mapp2 = defaultdict(int)
            
            for elm in words[i]:
                mapp2[elm] += 1
            
            for elm in mapp:
                if elm in mapp2:
                    mapp[elm] = min(mapp[elm],mapp2[elm])
                else:
                    mapp[elm] = 0
        
        for elm in mapp:
            for i in range(mapp[elm]):
                ans.append(elm)
        return ans