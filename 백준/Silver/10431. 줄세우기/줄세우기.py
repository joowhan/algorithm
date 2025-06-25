case = int(input())
answer = [0]*case
for _ in range(case):
    lis = list(map(int, input().split()))
    heights = lis[1:]
    tmp = [heights[0]]
    for i in range(1,20):
        tmp.append(heights[i])
        tmp.sort()
        answer[lis[0]-1] += len(tmp[tmp.index(heights[i])+1:])
    print(lis[0], answer[lis[0]-1])