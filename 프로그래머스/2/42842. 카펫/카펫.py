import math

def solution(brown, yellow):
    answer = []
    a = 1
    b = -(brown/2+2)
    c = brown+yellow
    d = (b**2)-(4*a*c)
    answer = [(-b+math.sqrt(d))/(2*a), (-b-math.sqrt(d))/(2*a)]
    return answer

