class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(set)
        net = 0

        for road in roads:
            adj[road[0]].add(road[1])
            adj[road[1]].add(road[0])
            
        for key in adj:
            for curr in adj:
                if len(adj[key]) >= len(adj[curr]) and curr != key:
                    temp = 0
                    if key in adj[curr]:
                        temp = len(adj[key]) + len(adj[curr]) - 1
                    else:
                        temp = len(adj[key]) + len(adj[curr]) 

                    net = max(net,temp)
                    curr = key
        return net