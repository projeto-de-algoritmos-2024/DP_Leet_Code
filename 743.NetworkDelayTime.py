from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')
        dist = [INF] * (n + 1)
        dist[k] = 0
        
        for _ in range(n - 1):
            updated = False
            for u, v, w in times:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break
        
        max_time = max(dist[1:])
        return max_time if max_time != INF else -1