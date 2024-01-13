def solution(elements):
    answer = 0
    # 길이가 1 ~ 5까지 가능
    n = len(elements)
    elements *=2
    result =set()
    
    for i in range(1,n+1): # 부분 수열 길이
        for j in range(n):
            result.add(sum(elements[j:j+i]))
    
    answer = len(result)
    return answer