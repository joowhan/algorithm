from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def solution(maps):
    answer = 0
    # 상대 진영에 최대한 빠르게 도착하기 
    # bfs로 최단 경로 찾기
    # 처음 위치는 항상 (1,1)
    n,m = len(maps), len(maps[0])
    queue = deque([(0,0)])
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            tx = x+dx[i]
            ty = y+dy[i]
            if tx<0 or tx>=n or ty<0 or ty>=m:
                continue
                
            if maps[tx][ty] == 1:
                queue.append((tx,ty))
                maps[tx][ty] =maps[x][y]+1
    answer = maps[-1][-1]
    if answer <=1:
        answer = -1
    return answer