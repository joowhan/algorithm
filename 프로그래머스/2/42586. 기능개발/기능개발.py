import math

def solution(progresses, speeds):
    answer = []
    # while len(progress):
    temp = [math.ceil((100-p)/s) for p, s in zip(progresses,speeds)]
    stack =[temp[0]]
    for i in range(1,len(temp)):
        if temp[i] > temp[i-1] and max(stack) < temp[i]:
            answer.append(len(stack))
            stack =[temp[i]]
        else:
            stack.append(temp[i])
    answer.append(len(stack))
    return answer