n = int(input())
people = []
answer = []

for _ in range(n):
    weight, height = map(int, input().split())
    people.append([weight, height])
for curr in people:
    rank = 1
    for other in people:
        if other[0] > curr[0] and other[1]>curr[1]:
            rank+=1
    answer.append(rank)
print(*answer)