def solution(records):
    answer = []
    visited ={}
    for record in records:
        info = record.split()
        if info[0] == 'Enter':
            visited[info[1]] = info[2]
        elif info[0] == 'Change':
            visited[info[1]] = info[2]
    for record in records:
        info = record.split()
        if info[0] == 'Change':
            continue
        elif info[0] == 'Enter':
            answer.append((visited[info[1]]+"님이 들어왔습니다."))
        elif info[0] =='Leave':
            answer.append((visited[info[1]]+"님이 나갔습니다."))
    return answer