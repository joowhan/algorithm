def solution(sequence, k):
    answer = [0, len(sequence)]
    left=0
    right = 0
    total = sequence[0]
    while True:
        if total < k:
            right +=1
            if right == len(sequence):
                break
            total += sequence[right]
        else:
            if total == k:
                if right-left < answer[1]-answer[0]:
                    answer = [left, right]
            total -= sequence[left]    
            left +=1
    return answer

