# 합승을 하거나, 안하거나 모두 가능. 
# 특정 지점까지만 합승하고 그 뒤로 따로 가는 것도 가능
# 현재 시점에서 a, b까지의 최단 경로와 각 노드에서 a, b까지의 최단 경로
import heapq
INF = int(1e9)

def dijkstra(start, end, graph):
    n = len(graph)
    distance=[INF]*(n+1)
    q=[]
    
    heapq.heappush(q, (start, 0))
    distance[start]=0
    
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] <dist:
            continue
        for i in graph[now]:
            cost =  distance[now]+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] =cost
                heapq.heappush(q, (i[0], cost))
    return distance[end]
        
def solution(n, s, a, b, fares):
    answer = 0
    graph=[[] for _ in range(n+1)]
    
    for fare in fares:
        x=fare[0];y=fare[1];z=fare[2];
        graph[x].append((y,z))
        graph[y].append((x,z))
    answer = dijkstra(s,a,graph) + dijkstra(s,b,graph)
    for k in range(1, n+1):
        if s !=k:
            answer = min(answer, dijkstra(s,k,graph) + dijkstra(k,a,graph)+ dijkstra(k,b,graph))
    
    return answer