# n개의 마을 중에서 k시간 이하로 걸리는 마을에게만 주문을 받을 예정
# road의 경우, a마을에서 b마을까지 c시간이 걸림을 의미

#최소 힙을 사용
import heapq

INF=int(1e9)

# 다익스트라 알고리즘으로 1번 마을에서 각 마을까지의 최단 경로 저장 후 k 이하만 count    
def solution(N, road, K):
    answer = 0
    q=[]
    distance=[INF]*(N+1) # 각 마을까지의 최단경로
    graph=[[] for _ in range(N+1)] # 각 마을이 어느 마을과 연결되어 있는지
    
    # road 정보를 graph에 넣기 -> 각 노드가 어느 노드와 연결되어 있는지 확인하기 위함
    for r in road:
        a=r[0]; b=r[1]; c=r[2];
        graph[a].append((b,c)) 
        graph[b].append((a,c))
    # q에 (현재 노드끼자의 최단 경로, 현재 노드 번호) 
    heapq.heappush(q, (0, 1))
    # 시작 마을은 늘 최단경로가 0
    distance[1]=0
    # dijkstra 탐색 시작
    while q:
        # min queue에서 가장 거리가 짧은 노드가 나옴
        dist, now = heapq.heappop(q)
        # 이미 처리된 적이 있는가?
        if distance[now] <dist:
            continue
        # 현재 노드와 연결된 다른 노드들 탐색.
        for i in graph[now]:
            # 현재 노드에서 연결된 다음 노드까지의 비용 계산
            cost = distance[now]+i[1]
            # 그 비용이 해당 노드까지 가는 기존 비용보다 더 적다면(즉, 최단경로라면)
            if cost < distance[i[0]]:
                # 최단 경로 업데이트
                distance[i[0]]=cost
                # heap에 추가
                heapq.heappush(q, (cost, i[0]))
    # 배달 시간이 k 이하인 노드들 갯수는?
    for dis in distance[1:]:
        if dis <=K:
            answer+=1
    return answer