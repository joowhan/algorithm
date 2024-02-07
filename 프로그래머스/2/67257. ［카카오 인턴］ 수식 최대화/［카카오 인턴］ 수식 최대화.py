import re
from itertools import permutations

def calculation(op,x,y):
    if op=='+':
        return int(x)+int(y)
    elif op=='*':
        return int(x)*int(y)
    else:
        return int(x)-int(y)

def solution(expression):
    answer = 0
    # 3가지 연산만으로 이루어진 수식 전달, 연산자의 우선순위를 자유롭게 재정의 가능 -> 만들 수 있는 가장 큰 수 제출
    # 2가지 연산자가 동일한 우선순위를 가질 수 없다. 
    # 가장 큰 상금을 return
    
    # 부호와 숫자를 분리 
    oper = [expression[i] for i in range(len(expression)) if not expression[i].isdigit()]
    lis = re.split(r'-|\*|\+',expression)
    priority = permutations(list(set(oper)))
    for p in priority:
        temp = oper.copy()
        nums = lis.copy()
        
        # print("oper: ",temp, " p: ",p)
        for op in p: 
            # print(op)
            while op in temp:
                i = temp.index(op)
                x,y = nums[i], nums[i+1]
                res = calculation(op, x,y)
                nums = nums[:i]+[res]+nums[i+2:]
                # print(nums)
                temp.remove(op)
                
                # print(temp)
        if abs(nums[0]) > answer:
            answer = abs(nums[0])
    return answer