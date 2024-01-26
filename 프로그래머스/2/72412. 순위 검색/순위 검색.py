from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(information, queries):
    answer = []
    # 초기화 값을 []로 설정
    dic = defaultdict(list)
    # 각 case를 모두 dictionary에 넣기 -> 이때 빈 값은 '-'로 대체해야 함
    for info in information:
        info = info.split()
        x = info[:-1]
        y = int(info[-1])
        # 모든 경우의 수 탐색 -> 모든 경우, 하나 뺀 경우, ...
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                temp = x.copy()
                for j in c:
                    temp[j] = '-'
                dic[''.join(temp)].append(y)
    
    for value in dic.values():
        value.sort()
    
    for query in queries:
        query = query.replace('and',"")
        query = query.split()
        k,v = ''.join(query[:-1]), int(query[-1])
        count = 0
        if k in dic:
            lis = dic[k]
            idx = bisect_left(lis, v)
            count = len(lis)-idx
        answer.append(count)
        
        
    return answer