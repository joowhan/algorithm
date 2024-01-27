from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []

    # 가장 많이 함께 주문한 단품 메뉴로 구성하기 
    for c in course:
        dic = defaultdict(int)
        max_val=[]
        for order in orders:
            temp = combinations(list(order),c)
            for k in temp:
                dic[''.join(sorted(k))]+=1
        # res = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        max_val = [k for k,v in dic.items() if v==max(dic.values()) and v>=2]
        answer.extend(max_val)
    return sorted(answer)