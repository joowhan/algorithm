n,k = map(int, input().split())
result = [0]*n
for i in range(n):
    lis = list(map(int, input().split()))
    result[lis[0]-1] = 100*lis[1]+10*lis[2]+1*lis[3]
print(sorted(result, reverse=True).index(result[k-1])+1)