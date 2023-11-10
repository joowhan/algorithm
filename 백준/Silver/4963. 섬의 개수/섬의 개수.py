from collections import deque
while True:
    w,h = map(int, input().split())
    if w==0 and h == 0:
        break
    graph=[]
    for i in range(h):
        graph.append(list(map(int, input().split())))
    
    visited = [[0]*w for _ in range(h)]
    count = 0
    
    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,1,-1,1,-1]
    
    for i in range(h):
        for j in range(w):
            queue = deque()
            if graph[i][j] == 1 and visited[i][j] == 0:
                queue.append([i,j])
                visited[i][j] = 1
                count +=1
                while queue:
                    x,y = queue.popleft()
                    for k in range(8):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if nx>=h or nx<0 or ny>=w or ny<0:
                            continue
                        if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            queue.append([nx,ny])
    print(count)