from typing import List
import heapq


class Solution:
    def find(self, parent: List[int], x: int) -> int:
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent: List[int], rank: List[int], x: int, y: int) -> bool:
        rootX = self.find(parent, x)
        rootY = self.find(parent, y)

        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True
        return False

    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        """
        LeetCode 3600. Maximize Spanning tree Stability with Upgrades

        1. 先放 must_use=1 的邊，再按 strength 大到小放其餘邊 (Max Spanning Tree)
        2. 用 min-heap 貪心 upgrade 最弱的可升級邊 (must_use=0 才能升級，strength 翻倍)
        3. 若最弱邊不可升級則直接回傳（upgrade 其他邊不會改善 min）
        """
        if len(edges) < n - 1:
            return -1

        # must_use=1 優先，同類中 strength 大的優先
        edges.sort(key=lambda x: (-x[3], -x[2]))

        parent = list(range(n))
        rank = [0] * n
        tree_edges = []

        for u, v, strength, must_use in edges:
            if self.union(parent, rank, u, v):
                tree_edges.append((strength, must_use))
            elif must_use == 1:
                return -1  # must_use 邊形成環

        # 檢查連通性
        root = self.find(parent, 0)
        for i in range(1, n):
            if self.find(parent, i) != root:
                return -1

        # min-heap: (strength, can_upgrade)
        # must_use=0 的邊才能 upgrade
        heap = [(s, 1 if m == 0 else 0) for s, m in tree_edges]
        heapq.heapify(heap)

        upgrades_used = 0
        while upgrades_used < k and heap:
            s, can_up = heapq.heappop(heap)
            if can_up:
                heapq.heappush(heap, (s * 2, 0))  # 升級後不能再升級
                upgrades_used += 1
            else:
                heapq.heappush(heap, (s, 0))
                break  # 最弱邊不可升級，upgrade 其他邊無法改善 min

        return heap[0][0]
