import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int, input().split()))
coordinate = set(lis)

temp = list(coordinate)
temp.sort()
sy = {temp[i]:i for i in range(len(temp))}
for i in range(n):
    print(sy[lis[i]], end=' ')