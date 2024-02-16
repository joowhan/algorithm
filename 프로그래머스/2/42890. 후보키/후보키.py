from itertools import combinations

def solution(relation):
    answer = 0
    # 후보키: 유일성, 최소성
    n = len(relation)
    m = len(relation[0])
    candidate = []
    for i in range(1, m+1):
        candidate.extend(combinations(range(m), i))
    
    unique=[]
    
    for c in candidate:
        temp = [tuple([item[j] for j in c]) for item in relation]
        flag = False
        if len(set(temp)) == n:
            flag = True
            for u in unique:
                if set(u).issubset(set(c)):
                    flag = False
                    break
        if flag == True:
            # answer +=1
            unique.append(c)
    answer = len(unique)
    return answer