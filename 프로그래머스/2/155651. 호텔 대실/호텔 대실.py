import heapq

def solution(book_time):
    answer = 1
    # 계속 갱신을 해야 하는지? 
    temp =[]
    for time in book_time:
         temp.append([int(time[0].replace(':','')), int(time[1].replace(':',''))])
    temp.sort()
    
    book_time_ref = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    book_time_ref.sort()
    
    heap = []
    for time in book_time_ref:
        if len(heap)==0:
            heapq.heappush(heap, time[1])
            continue
        # print("*현재 시작하는 시간, 방 쓰고 있는 사람",time[0], heap[0])
        # 만약 방을 쓰고 있는 사람이 나오는 시간 이후에 다음 사람이 대실한다면? -> 그 사람의 방을 그대로 사용 가능
        if heap[0] <= time[0]:
            # print("!", heap[0], time[0])
            heapq.heappop(heap)
        # 시간이 겹친다면? 
        else:
            answer +=1
            # print(heap[0], time[0])
        heapq.heappush(heap, time[1]+10)
        # print('힙', heap)
            
    # print(temp)
    
    return answer