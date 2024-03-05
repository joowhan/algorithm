
def solution(msg):
    answer = []
    dic = {}
    for i in range(26):
        dic[chr(65+i)] = i+1
    curr, p =0,0
    while True:
        curr +=1
        if curr == len(msg):
            answer.append(dic[msg[p:curr]])
            break
        if msg[p:curr+1] not in dic:
            dic[msg[p:curr+1]] = len(dic)+1
            answer.append(dic[msg[p:curr]])
            p = curr
            
    return answer