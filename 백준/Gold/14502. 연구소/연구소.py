n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
from itertools import combinations
import copy
from collections import deque

candidate=[]
virus=[]
answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            candidate.append((i,j))
        elif graph[i][j]==2:
            virus.append((i,j))

def bfs(virus, temp):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque(virus)
    cnt = 0
    while q:
        px, py  = q.popleft()
        for i in range(4):
            tx = px+dx[i]
            ty = py+dy[i]
            if 0<=tx<n and 0<=ty<m:
                if temp[tx][ty] ==0:
                    temp[tx][ty] = 2
                    q.append((tx,ty))
    cnt = 0
    for r in temp:
        cnt += r.count(0)
    return cnt

for k in combinations(candidate,3):
    temp = copy.deepcopy(graph)
    curr = 0
    for x in k:
        temp[x[0]][x[1]] = 1
    curr = bfs(virus, temp)
    answer = max(curr, answer)
print(answer)