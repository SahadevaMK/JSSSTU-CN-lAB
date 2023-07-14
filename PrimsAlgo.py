from heapq import *

def krushkal(graph):
        visited = set()
        source = 0
        heap= [(0,source, source)]
        ans = []
        while heap:
            w, node, parent = heappop(heap)
            if node not in visited:
                visited.add(node)
                if node!=parent:
                    ans.append((f"{parent}->{node}", w))
                for child,wt in graph[node]:
                    if child not in visited:
                        heappush(heap,(wt,child,node))
        ans.sort(key= lambda x: x[1])
        for edge, weight in ans:
            print(edge," : ",weight)
        
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}

krushkal(graph)