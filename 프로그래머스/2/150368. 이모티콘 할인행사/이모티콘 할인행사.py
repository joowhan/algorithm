from itertools import product

def solution(users, emoticons):
    answer = []
    discount=[10,20,30,40]
    for case in list(product(discount, repeat=len(emoticons))):
        res =[0,0]
        for user in users:
            tmp = 0
            for i, c in enumerate(case):
                # 유저가 기대한 할인 이상이면
                if c >=user[0]:
                    tmp += emoticons[i]*(100-c)//100
            if tmp >= user[1]:
                res[0]+=1
            else:
                res[1]+=tmp
        answer.append(res)
    answer.sort(key=lambda x: (-x[0], -x[1]))
    
    return answer[0]