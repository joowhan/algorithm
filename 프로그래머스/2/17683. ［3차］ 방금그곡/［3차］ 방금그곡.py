def solution(m, musicinfos):
    answer = '(None)'
    candidate = []
    
    for index, info in enumerate(musicinfos):
        start, end, song, melody = info.split(',')
        a, b = map(int, start.split(':'))
        c, d = map(int, end.split(':'))
        playtime = c * 60 + d - a * 60 - b
        
        melody_list = list(melody)
        for idx, mel in enumerate(melody_list):
            if mel == '#':
                melody_list[idx-1] += '#'
        melody_list = [mel for mel in melody_list if mel != '#']
        
        length = len(melody_list)
        real = ''
        for i in range(playtime):
            idx = i % length
            real += melody_list[idx]
            
        if m in real:
            if real.count(m) > real.count(m+'#'):
                candidate.append([playtime, song, index])
    
    if candidate:
        candidate.sort(key=lambda x:(-x[0], x[2]))
        return candidate[0][1]
    else:
        return answer