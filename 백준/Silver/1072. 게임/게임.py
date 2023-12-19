# 앞으로 모든 게임에서 지지 않는다 = X만 조절하면 된다. 
x,y = map(int, input().split())
z = (y*100)//x
# 절대 불가능한 경우
answer = x
if z>=99:
    print(-1)
else: 
    left, right = 0, x
    while left<=right:
        target = (left+right)//2
        if ((y+target)*100//(x+target))>z:
            answer = target
            right = target-1
        else:
            left = target +1
    print(answer)