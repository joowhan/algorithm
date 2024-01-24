def solution(numbers):
    answer = []
    for number in numbers:
        temp = list('0'+ bin(number)[2:])
        idx = ''.join(temp).rfind('0')
        temp[idx] = '1'
        if number%2 !=0:
            temp[idx+1] = '0'
        answer.append(int(''.join(temp),2))
    return answer