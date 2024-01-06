from collections import deque

def solution(x, y, n):
    answer = 0
    # dfs/bfs로 최소 연산 찾기
    visited=[0 for _ in range(y+1)]

    def dfs(x,y,n):
        minimum = int(1e9)
        queue = deque([])
        queue.append([x,0])
        visited[x] = 1
        while queue:
            t, cnt = queue.popleft()
            if t == y:
                if cnt < minimum:
                    minimum = cnt
            a,b,c = t+n,t*2, t*3
            if x<= a <=y and not visited[a]:
                visited[a] = 1
                queue.append([a, cnt+1])
            if x<= b <=y and not visited[b]:
                visited[b] = 1
                queue.append([b, cnt+1])
            if x<= c <=y and not visited[c]:
                visited[c] = 1
                queue.append([c, cnt+1])  
        return minimum
    answer = dfs(x,y,n)
    if answer == int(1e9):
        return -1
    return answer