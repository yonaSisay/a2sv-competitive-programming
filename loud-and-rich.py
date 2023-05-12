class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        ans = list(range(len(quiet)))
        graph = defaultdict(list)
        indg = defaultdict(int)

        for src,des in richer:
            graph[src].append(des)
            indg[des] += 1

        que = deque()

        for i in range(len(quiet)):
            if i not in indg:
                que.append(i)

        while que:
            temp = que.pop()

            for elm in graph[temp]:
                if quiet[ans[elm]] >= quiet[ans[temp]]:
                    ans[elm] = ans[temp]
                indg[elm] -= 1

                if not indg[elm]:
                    que.append(elm)
        
        return ans