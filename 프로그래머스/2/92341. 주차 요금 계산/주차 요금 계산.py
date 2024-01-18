import math

def solution(fees, records):
    answer = []
    
    # 기본 시간 180분 = 5000원 10분 당 600원
    # 출차가 없다면 시간은 23:59로 설정
    # 기본 시간 이하라면 기본 요금
    # 기본 시간 이상이면 추가 요금도 받는다. 이때 나눠떨어지지 않으면 올림
    
    default_t, default_fee, s_time, s_fee = fees[0], fees[1], fees[2], fees[3]
    cars={}
    result={}
    end_time = 23*60+59
    
    for info in records:
        t, num, io = info.split()
        hh, mm = t.split(':')
        time = int(hh)*60+int(mm)
        if io =='IN':
            cars[num] = time
        # 출차 했다면
        else:
            cars[num] = time - cars[num]
            if num in result.keys():
                result[num] += cars[num]
            else:
                result[num] = cars[num]
            cars[num] = -1
            
    for num in cars:
        if cars[num] !=-1:
            cars[num] = end_time - cars[num]
            if num in result.keys():
                result[num] += cars[num]
            else:
                result[num] = cars[num]    
            cars[num] = -1           
    
    for key in result:
        if result[key] <= default_t:
            result[key] = default_fee
        else:
            temp = default_fee + math.ceil((result[key]-default_t)/s_time)*s_fee
            result[key] = temp
    
    temp = sorted(result.items(), key=lambda x:x[0])
    answer = [x[1] for x in temp]
    return answer