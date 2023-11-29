from collections import deque

test_case = int(input())

for _ in range(test_case):
    # 가로, 세로, 배추 개수
    m,n,k = map(int, input().split())
    graph = [[0 for i in range(m)] for i in range(n)]
    visited = [[0 for i in range(m)] for i in range(n)]
    for _ in range(k):
        a,b = map(int, input().split())
        graph[b][a] = 1
        
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    cnt = 0
    for i in range(n):
        for j in range(m):
            queue = deque()
            if graph[i][j] == 1 and visited[i][j] ==0:
                queue.append([i,j])
                visited[i][j] = 1
                cnt +=1
            while queue:
                x,y = queue.popleft()
                for k in range(4):
                    nx = dx[k]+x
                    ny = dy[k]+y
                    if nx>=n or nx<0 or ny>=m or ny < 0:
                        continue
                    if graph[nx][ny] ==1 and visited[nx][ny]==0:
                        visited[nx][ny] = 1
                        queue.append([nx,ny])
    print(cnt)