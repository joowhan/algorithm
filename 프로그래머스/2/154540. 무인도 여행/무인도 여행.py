from collections import deque

def solution(maps):
    answer = []
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    m,n = len(maps[0]), len(maps)
    visited =[[0 for _ in range(m)] for _ in range(n)]
    
    def bfs(x,y):
        queue = deque([])
        queue.append([x,y])
        visited[x][y] = 1
        foods = int(maps[x][y])
        while queue:
            nx,ny = queue.popleft()
            for i in range(4):
                tx = nx+dx[i]
                ty = ny+dy[i]
                if tx >=n or tx<0 or ty>=m or ty<0:
                    continue
                if not visited[tx][ty] and maps[tx][ty] !='X':
                    foods += int(maps[tx][ty])
                    visited[tx][ty] = 1
                    queue.append([tx,ty])
        return foods
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(bfs(i,j))
    answer.sort()
    if answer:
        return answer
    else:
        answer.append(-1)
        return answer