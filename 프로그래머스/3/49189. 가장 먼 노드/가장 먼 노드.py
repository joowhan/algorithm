#플로이드 워샬 알고리즘? 다만 시간복잡도가 높은데..
# bfs로 탐색
from collections import deque
def solution(n, edge):
    answer = 0
    graph =[[] for _ in range(n+1)]
    for v in edge:
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])
    visited=[-1]*(n+1)
    q = deque([])
    q.append((1,0))
    visited[1] = 0
    while q:
        curr, dist = q.popleft()
        # if visited[curr] !=-1:
        #     continue
        for i in graph[curr]:
            if visited[i]==-1:
                visited[i] = dist+1
                q.append((i, dist+1))
    for x in visited:
        if x >=max(visited):
            answer +=1
    return answer