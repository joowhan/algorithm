from collections import deque

n, k  = map(int, input().split())

queue = deque([i for i in range(1, n+1)])
answer =[]
while queue:
    temp = (k-1)%len(queue)
    for t in range(temp):
        queue.append(queue.popleft())
    a = queue.popleft()
    answer.append(str(a))
print('<',', '.join(answer),'>', sep='')