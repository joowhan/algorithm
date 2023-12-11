import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(n)]


for i in range(n):
    graph[i] = [0]+ graph[i]
    for j in range(1, len(graph[i])):
        graph[i][j] += graph[i][j-1]

for _ in range(m):
    x1,y1, x2,y2 = map(int, input().split())
    temp = 0
    for i in range(x1-1, x2):
        temp += graph[i][y2] - graph[i][y1-1]
    print(temp)