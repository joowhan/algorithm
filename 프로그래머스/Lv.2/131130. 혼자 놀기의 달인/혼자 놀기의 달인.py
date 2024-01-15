from collections import deque

def solution(cards):
    answer = 0
    visited = [0 for _ in range(len(cards)+1)]
    # def bfs(x):
    result =[]
    for i in range(len(cards)):
        if not visited[i+1]:
            t = i+1
            temp = 1
            while True:
                if visited[t] == 1:
                    break
                visited[t] = 1
                if not visited[cards[t-1]]:
                    t = cards[t-1]
                    temp +=1
            result.append(temp)
    result.sort(reverse=True)
    if len(result)==1:
        return 0
    else:
        answer = result[0]*result[1]
    return answer