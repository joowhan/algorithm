import math

def solution(m, n, startX, startY, balls):
    answer = []
    # 가로, 세로, 공의 좌표(x,y), 목표 공의 좌표 모음
    # 친 공이 굴러간 거리의 최소값의 제곱
    # 입사각과 반사각은 동일, 꼭지점을 부딪히면 반대방향
    for ballX, ballY in balls:
        dist = []
        if not (ballX == startX and ballY > startY):
            d2 = (ballX - startX)**2 + (ballY - 2*n+startY)**2
            dist.append(d2)
        # 아래쪽 벽
        # 단, x좌표가 같고 목표의 y가 더 작으면 안된다.
        if not (ballX == startX and ballY < startY):
            d2 = (ballX - startX)**2 + (ballY + startY)**2
            dist.append(d2)
        # 왼쪽 벽에 맞는 경우
        # 단, y좌표가 같고 목표의 x가 더 작으면 안된다.
        if not (ballY == startY and ballX < startX):
            d2 = (ballX + startX)**2 + (ballY - startY)**2
            dist.append(d2)
        # 오른쪽 벽
        # 단, y좌표가 같고 목표의 x가 더 크면 안된다.
        if not (ballY == startY and ballX > startX):
            d2 = (ballX - 2*m+startX)**2 + (ballY - startY)**2
            dist.append(d2)
        answer.append(min(dist))
    return answer