def solution(order):
    answer = 0
    stack =[]
    i = 1
    k = 0
    
    n = len(order)
    while i != n+1:
        stack.append(i)
        while stack and stack[-1] == order[k]:
            answer +=1
            k+=1
            # print(stack)
            stack.pop()
            # print(stack)
        i+=1
    return answer