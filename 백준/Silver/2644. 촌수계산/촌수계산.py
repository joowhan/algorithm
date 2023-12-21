n = int(input())
a,b = map(int, input().split())
m = int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    p,c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)
from collections import deque

def bfs(x,y):
    queue = deque([])
    queue.append([x, 0])
    visited = [0 for _ in range(n+1)]
    visited[x] = 1
    while queue:
        curr, degree = queue.popleft()
        if curr == y:
            return degree
        for node in graph[curr]:
            if not visited[node]:
                visited[node] = 1
                queue.append([node, degree+1])
    return -1      
print(bfs(a,b))