import heapq

INF = int(1e9)
n,d = map(int, input().split())
    

graph = [[] for _ in range(d+1)]
distance = [INF for i in range(d+1)]


for i in range(d):
    graph[i].append((i+1, 1))

for i in range(n):
    a, b, c = map(int, input().split())
    if b > d:
        continue
    graph[a].append((b,c))

def dijkstra(start):
    queue=[]
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
dijkstra(0)
print(distance[d])