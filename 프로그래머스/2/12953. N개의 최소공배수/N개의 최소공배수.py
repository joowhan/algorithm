import math
def gcd(a,b):
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            return i       
        
def solution(arr):
    answer = arr[0]
    # n개의 수의 최소공배수
    # n개의 수 나누기 -> 1,2,3,4,....
    for a in arr:
        answer = (a*answer)//gcd(a, answer)
    return answer