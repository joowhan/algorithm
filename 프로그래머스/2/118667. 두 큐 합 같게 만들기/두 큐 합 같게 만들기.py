from collections import deque

def solution(queue1, queue2):
    answer = 0
    n = len(queue1)*3
    s1, s2 = sum(queue1), sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    while True:
        if s1 == s2:
            break
        if s1>s2:
            t = queue1.popleft()
            queue2.append(t)
            s1 -= t
            s2 += t
            answer +=1
        elif s1 < s2:
            t = queue2.popleft()
            queue1.append(t)
            s2 -= t
            s1 += t
            answer +=1
        if answer == n:
            return -1
            
    return answer