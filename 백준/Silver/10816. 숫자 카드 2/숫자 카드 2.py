n = int(input())
cards = list(map(int, input().split()))
m = int(input())
tmp = list(map(int, input().split()))

dic = {}
for c in cards:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1

for t in tmp:
    print(dic.get(t, 0), end=" ")
