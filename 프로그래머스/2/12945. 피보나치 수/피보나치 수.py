import sys
sys.setrecursionlimit(10**6)

def fibonacci(n):
    
    if n <2:
        return n
    return (fibonacci(n-1)%1234567+fibonacci(n-2)%1234567)%1234567

def solution(n):
    answer = []
    for i in range(n+1):
        if i<2:
            answer.append(i)
        else:
            temp = answer[i-1]+answer[i-2]
            answer.append(temp%1234567)
    return answer[n]