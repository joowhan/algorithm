from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(maps, target, x,y,n,m):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    # n,m = len(maps), len(maps[0])
    visited=[[0 for _ in range(m)] for _ in range(n)]
    rx,ry=0,0
    queue = deque([])
    queue.append([x,y,0])
    visited[x][y] = 1
    res = 100000
    while queue:
        nx, ny, cnt = queue.popleft()
        for i in range(4):
            tx = nx+dx[i]
            ty = ny+dy[i]
            if tx>=n or tx<0 or ty>=m or ty<0:
                continue
            if maps[tx][ty] != 'X' and not visited[tx][ty]:
                if maps[tx][ty] == target:
                    if cnt+1 <=res:
                        res = cnt + 1
                        rx,ry = tx,ty
                queue.append([tx,ty, cnt+1])
                visited[tx][ty] = 1
    return res,rx,ry 
def solution(maps):
    answer = 0
    n,m = len(maps), len(maps[0])
    # 래버를 당겨야지만 탈출이 가능하다. 따라서 먼저 래버가 있는 칸에 도달한 다음 exit 칸을 가는 것이 중요하다.
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                x,y = i,j
                break
    answer,lx,ly = bfs(maps,'L', x,y,n,m)
    if answer ==100000:
        return -1
    print(lx,ly)
    temp, lx,ly = bfs(maps,'E', lx,ly,n,m)
    if temp ==100000:
        return -1
    answer += temp
    return answer