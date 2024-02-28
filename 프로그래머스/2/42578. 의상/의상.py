from itertools import combinations
def solution(clothes):
    answer = 1
    closet = {}
    for cloth in clothes:
        if cloth[1] in closet.keys():
            closet[cloth[1]].append(cloth[0])
        else: 
            closet[cloth[1]] = [cloth[0]]
    for key in closet.keys():
        answer *= (len(closet[key])+1)
    return answer-1