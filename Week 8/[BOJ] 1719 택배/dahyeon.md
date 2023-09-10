```
<접근법>
플로이드워셜 알고리즘 사용
```
```python
import sys
from pprint import pprint
input = sys.stdin.readline
n,m = map(int, input().split())
INF = sys.maxsize
graph = [[INF]*(n+1) for _ in range(n+1)]
answer= [['-']*(n+1) for _ in range(n+1)]
for i in range(m):
    start, end, dis = map(int, input().split())
    graph[start][end]= dis
    graph[end][start]= dis
    answer[start][end] = end
    answer[end][start] = start



#step1: 자기자신
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0
     
#step2: 배열 생성
for i in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            if graph[start][end] > graph[start][i]+graph[i][end]:
                answer[start][end]=answer[start][i]
            graph[start][end]= min(graph[start][end],graph[start][i]+graph[i][end])
            

for arr in answer[1:]:
    print(*arr[1:])
```