### 코드
```
n = int(input())
adj = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(n-1):
    v1, v2 = map(int, input().split(' '))
    adj[v1].append(v2)
    adj[v2].append(v1)

for i in range(2, n+1):
    print(adj[i][0])
```
### 설명
- 시간 초과
- 인접리스트의 첫 엣지가 무조건 부모가 되지는 않음

### 코드
```
import sys

n = int(sys.stdin.readline())
adj = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(n-1):
    v1, v2 = map(int, sys.stdin.readline().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

def dfs(start):
    stack = [start]
    while stack:
        v = stack.pop()
        for i in adj[v]:
            if visited[i] == 0:
                visited[i] = v
                stack.append(i)

dfs(1)
for i in range(2, n+1):
    print(visited[i])
```

### 설명
- sys.stdin.readline() 사용하여 input 시간 절약
- dfs에 stack을 활용
- dfs를 통해 visited에 방문 기록을 남기고 하나씩 출력