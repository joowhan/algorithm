def solution(line):
    answer = []
    stars = set()
    for i in range(len(line)):
        temp = line[:i]+line[i+1:]
        a,b,e = line[i]
        for j in range(len(temp)):
            c,d,f = temp[j]
            if a*d-b*c ==0:
                continue
            else:
                x = (b*f-e*d)/(a*d-b*c)
                y = (e*c-a*f)/(a*d-b*c)
            if x == int(x) and y == int(y):
                stars.add((int(x),int(y)))
    stars = sorted(stars)
    
    w1, w2 = min(stars, key = lambda x : x[0])[0], max(stars, key = lambda x : x[0])[0] + 1
    h1, h2 = min(stars, key = lambda x : x[1])[1], max(stars, key = lambda x : x[1])[1] + 1
    
    # 별을 포함하는 최소한의 크기 배열 생성
    answer = [['.'] * (w2 - w1) for _ in range((h2 - h1))]
    for x,y in stars:
        answer[y-h1][x-w1] = '*'
    answer.reverse()
    # [''.join(a) for a in answer]
    return [''.join(a) for a in answer]