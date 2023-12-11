n,m = map(int, input().split())
lis = [0]+list(map(int, input().split()))
for k in range(1,n+1):
    lis[k] +=lis[k-1]
for k in range(m):
    i,j = map(int, input().split())
    i = i-1
    print(lis[j]-lis[i])