from collections import deque

def solution(priorities, location):
    answer = 0
    process = [(i, priorities[i])for i in range(len(priorities))]
    queue = deque(process)
    lis =[]
    while len(queue)>1:
        p, order = queue.popleft()
        if order < max(queue, key=lambda x:x[1])[1]:
            queue.append((p,order))
        # 가장 우선순위가 높다면
        else:   
            lis.append(p)
    lis.append(queue[0][0])
    answer = lis.index(location)+1
    return answer