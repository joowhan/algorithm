n = int(input())
a = list(map(int, input().split()))
m = int(input())
lis = list(map(int, input().split()))

a.sort()
for x in lis:
    if x in a:
        print(1)
    else:
        print(0)