from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    # 사람 무게 * 시소 축과 좌석 간 거리
    # 2의 공배수, 3의 공배수, 4의 공배수 구하기
    for c in counter:
        if counter[c] >=2:
            answer += counter[c]*(counter[c]-1)//2
    #2:3, 2:4, 3:4
    weights = set(weights)
    for weight in weights:
        if weight*2/3 in weights:
            answer += counter[weight*2/3]*counter[weight]
        if weight*2/4 in weights:
            answer += counter[weight*2/4]*counter[weight]
        if weight*3/4 in weights:
            answer += counter[weight*3/4]*counter[weight]
    # for i in range(len(weights)):
    return answer