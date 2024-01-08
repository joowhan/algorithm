def solution(data, col, row_begin, row_end):
    answer = 0
    n = len(data[0])
    data.sort(key=lambda x:(x[col-1], -x[0]))
    for i in range(row_begin-1, row_end):
        t = i+1
        temp = 0
        for j in range(n):
            temp += data[i][j]%t
        answer = answer ^ temp
    return answer