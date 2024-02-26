import heapq

def solution(prices):
    answer = []
    for i in range(len(prices)):
        curr =prices[i]
        temp = 0
        for j in range(i, len(prices)):
            if prices[j] < curr:
                temp +=1
                break
            else:
                temp +=1
        answer.append(temp-1)
            
    return answer