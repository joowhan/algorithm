
def convert_bin(s, zero, cnt):
    
    while True:
        if int('0b'+s,2) ==1:
            break
        one = s.count('1')
        zero += (len(s) - one)
        s = bin(one)[2:]
        cnt +=1
    
    return cnt,zero

def solution(s):
    answer = [0,0]
    # print(type(s))
    answer = convert_bin(s,0,0)
    return answer