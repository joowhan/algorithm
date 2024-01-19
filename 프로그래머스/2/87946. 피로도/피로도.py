answer = 0
def dfs(k, cnt, dungeons, visited):
    global answer 
    
    for i, dg in enumerate(dungeons):
        # 조건을 충족한다면? 
        if k >= dg[0] and not visited[i]:
            visited[i] = 1
            dfs(k-dg[1], cnt+1,dungeons, visited)
            visited[i] = 0
    if cnt > answer:
        answer = cnt

def solution(k, dungeons):
    global answer
    visited = [0 for _ in range(len(dungeons))]
    dfs(k,0,dungeons, visited)
    return answer