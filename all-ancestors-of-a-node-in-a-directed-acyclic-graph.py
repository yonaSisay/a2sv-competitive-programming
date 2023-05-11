class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indgree = defaultdict(int)

        for source, end in edges:
            graph[source].append(end)
            indgree[end] += 1
        que = deque()

        for i in range(n):
            if i not in indgree:
                que.append(i)
        ans = [set() for _ in range(n)]

        while que:
            temp = que.popleft()
            
            for elm in graph[temp]:
                indgree[elm] -= 1
                ans[elm].add(temp)
                ans[elm] = set(sorted(list(ans[elm].union(ans[temp]))))

                if not indgree[elm]:
                    que.append(elm)

        return [sorted(list(arr)) for arr in ans]