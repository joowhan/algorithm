# 각 지역은 유일한 번호로 구분 가능, 두 지역 통과 길이는 1
# 부대원 위치 순서대로 복귀할 수 있는 최단경로
from collections import deque


# 총 지역, 길 정보, 부대원 위치, 목적지
def solution(n, roads, sources, destination):
    answer = []
    graph=[[] for _ in range(n+1)]
    
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])

    visited = [-1]*(n+1)
    visited[destination] =0
    q = deque([destination])

    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i]==-1:
                visited[i] =visited[x]+1
                q.append(i)
    for source in sources:
        answer.append(visited[source])   
#     for source in sources:
#         visited = [-1]*(n+1)
#         visited[source] =0
#         q = deque([source])

#         while q:
#             x = q.popleft()
#             for i in graph[x]:
#                 if visited[i]==-1:
#                     visited[i] =visited[x]+1
#                     q.append(i)
#         answer.append(visited[destination])
    return answer