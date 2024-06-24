
def solution(triangle):
    answer = 0
    height=len(triangle)
    for h in range(height-2,-1,-1):
        for i in range(len(triangle[h])):
            triangle[h][i] += max(triangle[h+1][i], triangle[h+1][i+1])
    answer = triangle[0][0]
    return answer