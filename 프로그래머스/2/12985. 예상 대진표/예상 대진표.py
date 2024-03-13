import math
def solution(n,a,b):
    answer = 1
    # a와 b는 항상 이긴다.
    while True:
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        if a==b:
            break
        answer +=1

    return answer