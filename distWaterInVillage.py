# Time: O((m+n)log(m+n))
# Space:O(m+n) for pipes and well edges, parent(n) and recursive stack find (n)
# Leetcode: Yes
# Issues: None

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # store ultimate parents
        parent = [i for i in range(n+1)]

        # add pipe edges and then add well edges as 0
        edges = []
        for pipe in pipes:
            edges.append(pipe)
        
        for i in range(1,n+1):
            edges.append([0,i,wells[i-1]])

        # sort edges for kruskals mst
        result = 0
        edges.sort(key = lambda x: x[2])

        def find(x):
            if parent[x] != x:                  # if parent not  ultimate parent
                parent[x] = find(parent[x])     # find ultimate
            return parent[x]

        # unionize
        for edge in edges:
            x = edge[0]
            y = edge[1]

            px = find(x)            # find parent of x
            py = find(y)            # find parent of y

            if px != py:            # if different parents? unionize
                result += edge[2]
                parent[py] = px
        
        return result

# Primms algorith// Heap based logic // O((m+n)log(m))/ O(m+n)

import heapq
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        # add pipe eges and then add well edges as 0
        edges = []
        for pipe in pipes:                      # add edges
            edges.append(pipe)
        
        for i in range(1,n+1):                  # 0 as edges
            edges.append([0,i,wells[i-1]])

        # store adjacency list
        hmap = {}        
        for edge in edges:
            if edge[0] not in hmap:
                hmap[edge[0]] = []
            if edge[1] not in hmap:
                hmap[edge[1]] = []
            hmap[edge[0]].append((edge[2],edge[1]))
            hmap[edge[1]].append((edge[2],edge[0]))                


        # create a priority queue // COST ALWAYS GOES FIRST IN PQ SINCE IT DETERMINES ORDER
        pq = []
        heapq.heappush(pq,(0,0))
        result = 0
        visited = [False] * (n+1)

        while pq:
            cost,node = heapq.heappop(pq)

            if visited[node]:
                continue
            
            visited[node] = True    
            result += cost

            for cost, ne in hmap[node]:
                if not visited[ne]:
                    heapq.heappush(pq, (cost, ne)) 


        return result
