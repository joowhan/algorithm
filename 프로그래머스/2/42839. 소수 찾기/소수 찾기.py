from itertools import permutations

def is_decimal(num):
    if num <=1:
        return False
    for i in range(1, num+1):
        if num % i ==0:
            if i == 1 or i == num:
                continue
            else:
                return False
    # print(num)
    return True
def solution(numbers):
    answer = 0
    candidate=[]
    numbers = list(numbers)
    for i in range(1, len(numbers)+1):
        temp = permutations(numbers,i)
        candidate.extend(list(temp))
    
    nums = set()
    for can in candidate:
        nums.add(int(''.join(list(can))))
    for n in nums:
        # print(int(''.join(list(can))))
        if is_decimal(n):
            answer +=1
    return answer