def solution(want, number, discount):
    answer = 0
    # 10일 동안 회원 자격
    n = len(discount)
    for i in range(n-10+1):
        temp = discount[i:i+10]
        # print(i+1, temp)
        flag = 0
        for j in range(len(want)):
            if temp.count(want[j]) < number[j]:
                flag = 1
                break
        if flag ==0:
            # print(i+1)
            answer +=1
            
            
            
        
    return answer