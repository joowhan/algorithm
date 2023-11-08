from collections import deque
import sys

T = int(sys.stdin.readline())

for t in range(T):
    m,n,k = map(int, sys.stdin.readline().split())
    #가로, 세로, 배추개수
    board = [[0 for i in range(m)] for i in range(n)]
    for i in range(k):
        x,y = map(int, sys.stdin.readline().split())
        board[y][x] = 1
    visited = [[0 for i in range(m)] for i in range(n)]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    count = 0
    for i in range(n):
        for j in range(m):
            q = deque()
            if board[i][j] == 1 and visited[i][j] == 0:
                count += 1
                visited[i][j] = 1
                q.append([i,j]) #y,x
            while q:
                y,x = q.popleft()
                for idx in range(4):
                    nx = x + dx[idx]
                    ny = y + dy[idx]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if visited[ny][nx] == 0 and board[ny][nx] == 1:
                        visited[ny][nx] = 1
                        q.append([ny,nx])
    print(count)