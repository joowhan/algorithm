import sys
sys.setrecursionlimit(10**7)

# 방향 순서: 'd', 'l', 'r', 'u' (사전순 기준)
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
directions = ['d', 'l', 'r', 'u']

answer = None  # 최종 답 저장용, None 초기화

def is_valid(x, y, n, m):
    return 1<=x<=n and 1<=y<=m

#path는 현재까지 누적 명령어, moves = 현재까지 이동한 횟수
def dfs(n, m, x, y, r, c, k, path, moves):
    global answer
    dist = abs(x-r) + abs(y-c)
    # 현재까지 이동거리와 맨해튼 거리가 k보다 크면 가지치기
    if dist+moves > k:
        return
    if moves ==k and x==r and y==c:
        if answer is None or path < answer:
            answer = path
        return
    # 사전 순 탐색
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if is_valid(nx,ny,n,m):
            if answer is not None and path+directions[i] >= answer:
                continue
            dfs(n,m,nx,ny,r,c,k,path+directions[i], moves+1)

def solution(n, m, x, y, r, c, k):
    global answer
    answer = None
    dist = abs(x-r) + abs(y-c)
    if dist >k or (k-dist)%2 ==1:
        return "impossible"
    dfs(n, m, x, y, r, c, k, "",0)
    if answer is None:
        return "impossible"
    return answer
