n,k = map(int, input().split())
score = [list(map(int, input().split())) for _ in range(n)]
score.sort(key=lambda x: (x[1],x[2],x[3]), reverse=True)
selected = [score[i][0] for i in range(n)].index(k)
for i in range(n):
    if score[selected][1:] == score[i][1:]:
        print(i+1)
        break