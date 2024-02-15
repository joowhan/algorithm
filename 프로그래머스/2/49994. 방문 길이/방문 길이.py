def solution(dirs):
    answer = 0
    # U, R, D, L
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    visited = set()
    x=0
    y=0
    
    for dir in dirs:
        if dir == 'U':
            nx = x + dx[0]
            ny = y + dy[0]
        elif dir == 'R':
            nx = x + dx[1]
            ny = y + dy[1]
        elif dir == 'D':
            nx = x + dx[2]
            ny = y + dy[2]
        elif dir == 'L':
            nx = x + dx[3]
            ny = y + dy[3]
            
        if -5<=nx<=5 and -5<=ny<=5:
            visited.add((x,y,nx,ny))
            visited.add((nx,ny,x,y))
            x,y=nx,ny
    answer = len(visited)//2
    return answer