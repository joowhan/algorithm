import sys
from collections import deque


n,m = map(int, input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [False]*(n+1)

def bfs(graph, start,visited):
    q = deque([start])
    while q:
        curr = q.popleft()
        for node in graph[curr]:
            if not visited[node]:
                q.append(node)
                visited[node]= True
cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt+=1
print(cnt)