import sys
input = sys.stdin.readline

# 1차 서류 심사, 2차 면접 시험
# 두 시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는다 -> 2개의 시험 모두 점수가 낮다면 탈락
# tc = test case
tc = int(input())

for _ in range(tc):
    n = int(input())
    test=[]
    count = 1
    for _ in range(n):
        a, b = map(int, input().split())
        test.append([a,b])
    test.sort()
    # blist = list(zip(*test))[1]
    # for i in range(1,n):
    #     if min(blist[:i]) > blist[i]:
    #         count +=1
    max_ = test[0][1]
    for i in range(1,n):
        if test[i][1] < max_:
            count +=1
            max_ = test[i][1]
    print(count)

