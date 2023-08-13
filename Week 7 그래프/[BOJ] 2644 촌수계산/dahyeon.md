```
메모리 : 34128 kb
시간 : 64ms
```
```python
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
t1,t2 = map(int, input().strip().split())
m = int(input())
q= deque()
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

#그래프 생성
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#그래프 탐색
def bfs():
    while q:
        x= q.popleft()
        for i in graph[x]:
            if visited[i]==0:
                visited[i]= visited[x]+1
                q.append(i)

q.append(t1)
visited[t1]=1
bfs()
#print(visited)
result = visited[t2]-1 if visited[t2]!=0 else -1

print(result)
```

