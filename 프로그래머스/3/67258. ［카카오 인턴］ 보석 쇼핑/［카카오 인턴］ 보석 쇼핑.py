# two pointer로 문제 해결 가능..
def solution(gems):
    answer = [0, len(gems)]
    all_gems = set(gems)
    size = len(all_gems)
    gem_dict = {gems[0]:1}
    left, right = 0,0
    while left < len(gems) and right < len(gems):
        # 해당 범위에 모든 보석이 들어 있으면? -> left를 이동
        if len(gem_dict) == size:
            # 가장 짧은 구간이면 업데이트
            if right-left < answer[1]-answer[0]:
                answer = [left, right]
            else:
                gem_dict[gems[left]] -=1
                if gem_dict[gems[left]] <=0:
                    del gem_dict[gems[left]]
                left +=1
        # 모든 보석이 없다면 ->right 이동
        else:
            right +=1
            if len(gems) == right:
                break
            if gems[right] in gem_dict:
                gem_dict[gems[right]] +=1
            else:
                gem_dict[gems[right]] =1

    return [answer[0]+1,answer[1]+1]