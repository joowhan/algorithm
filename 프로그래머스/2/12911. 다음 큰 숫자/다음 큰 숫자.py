import sys
input = sys.stdin.readline()

def solution(n):
    answer = 0
    # n 보다 크면서 2진수로 변환 했을 때 1의 개수가 같은 수 중에서 최소값.
    k = n
    while True: 
        k +=1
        if (bin(n)[2:]).count('1') == (bin(k)[2:]).count('1'):
            return k