from collections import deque

def solution(operations):
    answer = [0,0]
    
    min_val = int(1e9)
    max_val = int(1e9)
    
    queue = deque([])
    for op in operations:
        cmd, val = op.split()
        if cmd =='I':
            queue.append(int(val))
        else:
            if len(queue)>0:
                if cmd=='D' and val=='-1':
                    queue.remove(min(queue))
                elif cmd=='D' and val=='1':
                    queue.remove(max(queue))
    if len(queue)>0:
        answer[0], answer[1] = max(queue), min(queue)
    return answer