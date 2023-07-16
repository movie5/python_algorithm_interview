```
def solution(genres, plays):
    idx_hsh = {} 
    genre_hsh = {}
    play_hsh = {}
    for i in range(len(genres)):
        idx_hsh[i] = [genres[i], plays[i]]
    idx_hsh = sorted(idx_hsh.items(), key=lambda x: x[1][1], reverse=True)
    # print(idx_hsh)
    # >>> [(4, ['pop', 2500]), (3, ['classic', 800]), (1, ['pop', 600]), (0, ['classic', 500]), (2, ['classic', 150])]
    for i, (genre, play) in idx_hsh:
        if genre not in genre_hsh:
            genre_hsh[genre] = [i]
        else:
            genre_hsh[genre].append(i)
        if genre not in play_hsh:
            play_hsh[genre] = play
        else:
            play_hsh[genre] += play
    # print(play_hsh)
    # >>> {'pop': 3100, 'classic': 1450}
    # print(genre_hsh)
    # >>> {'pop': [4, 1], 'classic': [3, 0, 2]}
    play_hsh = sorted(play_hsh.items(), key=lambda x: x[1], reverse=True)
    # print(play_hsh)
    # >>> [('pop', 3100), ('classic', 1450)]
    answer = []
    for clss, _ in play_hsh:
        answer.append(genre_hsh[clss][0])
        if len(genre_hsh[clss]) > 1:
            answer.append(genre_hsh[clss][1])
    return answer
```

### 풀이
- idx, genre, play에 대한 해시를 만들어줌
- {idx: {genre: [], play: []}}
- 모든 노래의 재생 횟수 순으로 정렬
- 인덱스를 genre_hsh에 append 하면 자연스럽게 장르 내에서 재생 횟수 순으로 정렬됨
- 장르별로 재생 횟수를 모두 더해서 정렬
- answer 리스트에 앞선 장르부터 골라 해당 장르의 첫 번째 곡을 append 1번 조건
- 해당 장르의 곡이 2곡 이상일 경우 해당 장르의 두 번째 곡을 append 2번 조건
- 장르와 재생 횟수가 같을 경우 이미 고유 번호 순으로 정렬되어 있으므로 자연스럽게 3번 조건 해결