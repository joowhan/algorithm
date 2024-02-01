import heapq

def solution(n, k, enemy):
    answer = k
    temp = enemy[:k]
    heapq.heapify(temp)
    for i in range(k, len(enemy)):
        heapq.heappush(temp, enemy[i])
        t = heapq.heappop(temp)
        n -= t
        if n <0:
            return answer
        answer +=1
    return len(enemy)