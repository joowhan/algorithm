from collections import deque

def bfs(place):
    developers=[]
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                developers.append([i,j])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    for x,y in developers:
        visited=[[0 for _ in range(5)] for _ in range(5)]
        queue=deque([])
        queue.append([x,y,0])
        visited[x][y] = 1
        
        while queue:
            nx,ny,cnt = queue.popleft()
            
            for i in range(4):
                tx = dx[i]+nx
                ty = dy[i]+ny
                
                if tx>=5 or tx<0 or ty>=5 or ty<0:
                    continue
                    
                if not visited[tx][ty] and place[tx][ty] =='O':
                    queue.append([tx,ty,cnt+1])
                    visited[tx][ty] = 1
                
                if not visited[tx][ty] and place[tx][ty] =='P':
                    visited[tx][ty]=1
                    if cnt <=1:
                        print(tx,ty)
                        return 0
    return 1
    
def solution(places):
    answer = []
    # 맨허튼 거리 2 이하 금지
    for place in places:
        answer.append(bfs(place))
    return answer