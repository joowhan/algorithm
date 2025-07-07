def solution(targets):
    answer = 0
    m=0
    targets.sort(key=lambda x:x[1])
    for i in range(len(targets)):
        if targets[i][0] < m:
            continue
        m = targets[i][1]
        answer +=1
    return answer