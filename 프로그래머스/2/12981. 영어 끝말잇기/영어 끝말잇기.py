def solution(n, words):
    answer = []
    
    m = len(words)
    prev = set()
    con = words[0][-1]
    # 차례
    c = 1
    prev.add(words[0])
    for i in range(1, len(words)):
        a = (i+1)%(n)
        if a ==0:
            a = n
        elif a==1:
            c +=1
        if words[i] in prev or con != words[i][0] or len(words)==1:
            answer = [a,c]
            break
        else:
            prev.add(words[i])
            con = words[i][-1]
    if len(answer) ==0:
        answer = [0,0]
    return answer