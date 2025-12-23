from collections import deque
def solution(s):
    answer = True
    q = deque([])
    for k in s:
        if k=='(':
            q.append(k)
        else:
            if len(q)==0:
                return False
            else:
                c = q.popleft()
    if len(q)!=0:
        return False
    return True