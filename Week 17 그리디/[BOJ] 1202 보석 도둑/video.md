# 오답
```
import bisect

N, K = map(int, input().split())
jewel = [list(map(int, input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]

jewel.sort(key=lambda x: -x[1])
bag.sort()

result = 0
for m, v in jewel:
    index = bisect.bisect_left(bag, m)
    if index >= result:
        result += 1

print(result)
```
- 예제는 다 맞았는데 오답
- 결국 우선순위 큐를 써야 함   
<br/>

# 정답
```
import heapq

N, K = map(int, input().split())
jewel = [list(map(int, input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]

jewel.sort()
bag.sort()

result = 0
heap = []
for b in bag:
    while jewel and jewel[0][0] <= b:
        heapq.heappush(heap, -jewel[0][1])
        heapq.heappop(jewel)

    if heap:
        result -= heapq.heappop(heap)

print(result)
```
- Python 3로 제출하면 시간초과
- PyPy3로 제출하면 정답