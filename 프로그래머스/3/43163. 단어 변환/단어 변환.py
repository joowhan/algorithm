from collections import deque
# 단어 1개를 바꾼다. -> words에 있는지 확인 -> 있으면 queue에 집어넣기
# queue에서 하나 꺼낸다. -> target과 일치한다면 return count
# 단어 변경 규칙 -> 1개씩을 제외한 단어를 포함하고 있는지 매번 검사..?

def bfs(begin, target, words):
    queue = deque([])
    queue.append([begin,0])
    count  =0
    while queue:
        curr, cnt = queue.popleft()
        if curr == target:
            return cnt
        
        for word in words:
            c = 0
            for i in range(len(curr)):
                if curr[i] !=word[i]:
                    c+=1
            if c == 1:
                queue.append([word, cnt+1])


def solution(begin, target, words):
    answer = 0
    if target in words:
        answer = bfs(begin, target, words)
    return answer