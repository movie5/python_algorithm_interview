# 정답
```
l, w, h = map(int, input().split())
n = int(input())
cube = [list(map(int, input().split())) for _ in range(n)]
cube = sorted(cube, reverse=True)

total = l * w * h

answer, tmp = 0, 0
for cube_ex, cube_cnt in cube:
    tmp *= 8 # 이전 정육면체*8이면 다음 정육면체의 면적 / 가장 큰 cube이므로 처음엔 0
    cube_len = 2**cube_ex

    remain = (l//cube_len)*(h//cube_len)*(w//cube_len)-tmp
    remain = min(cube_cnt, remain)

    answer += remain
    tmp += remain

if tmp == total:
    print(answer)
else:
    print(-1)
```
- 먼저 전체 면적을 구함
- 가장 큰 cube부터 greedy하게 상자의 면적을 차지
- tmp에는 이전 루프 크기의 정육면체를 현재 루프 크기의 정육면체로 몇개까지 커버할 수 있을지를 나타냄(8배)
- remain은 (전체 상자의 각 사이즈를 큐브 한 변의 길이로 나눈 공간) - (이전 루프 크기의 정육면체가 차지하고 있던 크기)
- remain과 해당 사이즈 큐브 개수 중 최소인 것이 answer에 누적
- 이미 상자의 공간을 차지하고 있기 때문에 다음 루프에 이것을 반영(tmp에 누적)
- 다음 사이즈의 큐브 루프에서 전체 상자 크기를 다시 해당 큐브를 쌓고 tmp를 빼줌
- 반복