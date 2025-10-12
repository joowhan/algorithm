from collections import defaultdict

def solution(genres, plays):
    answer = []
    # 장르 별 가장 많이 재생된 노래 2개씩 
    # 가장 많이 재생된 장르
    # 가장 많이 재생된 노래 
    genre_play = defaultdict(int)
    genre_song = defaultdict(list)
    
    for i, (g,p) in enumerate(zip(genres,plays)):
        genre_play[g] +=p
        genre_song[g].append((p, i))
    sorted_play = sorted(genre_play.items(), key=lambda x:x[1], reverse=True)
    for k, _ in sorted_play:
        s = sorted(genre_song[k], key=lambda x:(-x[0],x[1]))
        for song in s[:2]:
            answer.append(song[1])
    return answer