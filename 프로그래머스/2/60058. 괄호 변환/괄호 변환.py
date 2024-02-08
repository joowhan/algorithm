def correct(u):
    if u[0] == '(':
        return True
    
def check(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt +=1
        elif s[i] ==')':
            cnt -=1
        if cnt ==0:
            return s[:i+1], s[i+1:]

def solution(p):
    return recursion(p)

def recursion(p):
    answer = ''
    # 1.
    if p=='':
        return ''
    u, v = check(p)
    if correct(u):
        return u+solution(v)
    else:
        answer = '(' + solution(v) + ')'
        for char in u[1:-1]:
            if char == '(':
                answer += ')'
            else:
                answer += '('
        return answer