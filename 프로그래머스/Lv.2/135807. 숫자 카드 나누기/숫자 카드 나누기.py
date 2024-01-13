from math import gcd

def solution(arrayA, arrayB):
    answer = 0
    
    gcdA = arrayA[0]
    for n in arrayA:
        gcdA = gcd(gcdA, n)
    
    gcdB = arrayB[0]
    for n in arrayB:
        gcdB = gcd(gcdB, n)
    
    k = len(arrayA)
    print(gcdA, gcdB)
    
    f1, f2 =1,1
    for i in range(k):
        if arrayA[i] % gcdB == 0:
            f1 = 0
        if arrayB[i] % gcdA ==0:
            f2 = 0
    if f1 == 0 and f2==0:
        answer = 0
    elif gcdA > gcdB:
        answer = gcdA
    elif gcdA == gcdB:
        answer = 0
    else:
        answer = gcdB

    return answer