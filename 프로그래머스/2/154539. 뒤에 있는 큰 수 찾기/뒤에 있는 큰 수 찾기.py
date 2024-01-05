def solution(numbers):
    answer = []
    dic = {}
    
    for i in range(len(numbers)):
        temp = -1
            
        for j in range(i, len(numbers)):
            if numbers[j]>numbers[i]:
                temp = numbers[j]
                break
        answer.append(temp)
    return answer