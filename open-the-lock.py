class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        q = deque([[0,0,0,0]])
        visited = set()
        visited.add("0000")

        level = 0

        def gen(tempp, i):
            res = []
            for j in [-1,1]:
                temp = tempp[:]
                if temp[i] == 0 and j == -1:
                    temp[i] = 9
                elif temp[i] == 9 and j == 1:
                    temp[i] == 0
                else:
                    temp[i] += j
                res.append(temp[:])
            return res
                
        stri = lambda temp: "".join(list(map(str, temp)))

        while q:
            N = len(q)

            for _ in range(N):
                temp  = q.popleft()

                if stri(temp) in deadends:
                    return -1

                if stri(temp) == target: return level

                for i in range(4):
                    arr = gen(temp[:], i)

                    for elm in arr:
                        if stri(elm) not in visited and stri(elm) not in deadends:
                            visited.add(stri(elm))
                            q.append(elm)
            level += 1

        return -1