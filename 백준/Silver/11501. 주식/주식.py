t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    max_price = 0
    answer = 0
    for i in range(len(lis)-1,-1,-1):
        if lis[i] > max_price:
            max_price = lis[i]
        else: 
            answer += max_price - lis[i]
    print(answer)