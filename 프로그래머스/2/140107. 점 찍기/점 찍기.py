import math

def solution(k, d):
    answer = 0
    for x in range(0,d+1, k):
        temp = math.floor(math.sqrt(d**2-x**2))
        answer += temp//k+1
    return answer