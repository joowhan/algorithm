import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int, input().split()))

lis.sort()

answer =0
for i in range(n+1):
    answer+=sum(lis[:i])
    # print(lis[:i])
print(answer)