n = int(input())
m = int(input())
computers = [[] for _ in range(n+1)]

for i in range(m):
    x,y = map(int, input().split())
    computers[x].append(y)
    computers[y].append(x)
visited= [False]*(n+1)

from collections import deque

q = deque([])
q.append(1)
visited[1] = True
answer = 0
while q:
    curr = q.popleft()
    for i in computers[curr]:
        if not visited[i]:
            visited[i] =True
            q.append(i)
            answer +=1
print(answer)