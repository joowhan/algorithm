n,m = map(int, input().split())
graph=[]
cctv=[]
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(m):
        if row[j] in [1,2,3,4,5]:
            cctv.append([row[j], i, j])
mode =[
    [],
    #1. 4가지
    [[0],[1],[2],[3]],
    #2. 2가지
    [[0,1],[2,3]],
    #3. 4가지
    [[0,3],[1,2],[1,3],[0,2]],
    #4. 4가지
    [[0,2,3],[0,1,2],[1,2,3],[0,1,3]],
    #5. 1가지
    [[0,1,2,3]]
]

#위, 아래, 왼쪽, 오른쪽
dx = [-1,1,0,0]
dy = [0,0,-1,1]

import copy

def fill(graph, mode, x,y):
    #정해진 방향(1차원 배열의 요소)
    for i in mode:
        # 시작점
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx >=n or nx<0 or ny>=m or ny <0:
                break
            if graph[nx][ny] == 6:
                break
            elif graph[nx][ny] == 0:
                graph[nx][ny] = -1
        

# 현재 어느 cctv, graph 전체(업데이트된)
def dfs(depth, graph):
    global minimum
    #모든 cctv로 경로 탐색을 마쳤다면?
    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += graph[i].count(0)
        minimum = min(count, minimum)
        return
    
    temp = copy.deepcopy(graph)
    cctv_num, x,y = cctv[depth]
    for i in mode[cctv_num]:
        # 현재 graph, 탐색 방향(1차원배열), cctv 초기 위치
        fill(temp, i, x,y)
        # 다음 cctv로 탐색
        dfs(depth+1, temp)
        temp = copy.deepcopy(graph)
    
minimum = int(1e9)
dfs(0, graph)
print(minimum)