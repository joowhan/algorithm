from collections import deque
def solution(board):
    answer = -1
    dest = []
    n,m = len(board), len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'G':
                dest =[i,j]
            elif board[i][j] =='R':
                start=[i,j]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    def bfs():
        cnt = 0
        queue = deque([])
        queue.append([start[0], start[1]])
        visited[start[0]][start[1]] = 1
        while queue:
            x,y = queue.popleft()
            if board[x][y] == 'G':
                return visited[x][y]-1
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                while True:
                    if nx >=n or nx<0 or ny>=m or ny<0:
                        break
                    elif board[nx][ny] == 'D':
                        break
                    else:
                        nx += dx[i]
                        ny += dy[i]
                # 벽이나, 게임판을 벗어나면 멈춤
                nx -=dx[i]
                ny -=dy[i]
                if not visited[nx][ny]:
                    visited[nx][ny] =visited[x][y]+1
                    cnt +=1
                    queue.append([nx,ny])
        return -1
    answer = bfs()
    if answer > 0:
        return answer
    else:
        return -1
    return answer