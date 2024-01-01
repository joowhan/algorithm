def solution(plans):
    answer = []
    # 시작하는 시간에 맞춰 시작하기
    # 진행 중 새로운 과제가 있으면 새로운 과제 실행 -> stack에 기존 과제 저장
    # 시간 내에 과제가 끝나면 result에 넣기, stack에서 과제 빼기
    
    # 시간 계산
    for plan in plans:
        h, m = plan[1].split(':')
        plan[1], plan[2] = int(h)*60+int(m), int(plan[2])
    plans.sort(key=lambda x: x[1])
    
    stack=[plans[0]]
    start_time = plans[0][1]
    # 만약 시간이 초과되면?
    # 30 90 남은 30분으로 가장 최근에서 값 빼기 
    for i in range(1, len(plans)):
        # stack에 작업이 남아 있는지?
        while stack:
            subject, start, time = stack.pop()
            if start_time < start:
                start_time = start
            # 만약 시간이 초과된다면 
            if (start_time+time) > plans[i][1]:
                stack.append([subject, start,  (start_time+time) - plans[i][1]])
                start_time = plans[i][1]
                break
            else:
                answer.append(subject)
                start_time += time
        stack.append(plans[i])
    while stack:
        answer.append(stack.pop()[0])
    return answer