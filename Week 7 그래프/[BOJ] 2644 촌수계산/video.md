### 코드
```
n = int(input())
beggin, target = map(int, input().split(' '))
m = int(input())

adj = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    fam1, fam2 = map(int, input().split(' '))
    adj[fam1].append(fam2)
    adj[fam2].append(fam1)

result = []

# 현재 노드, 현재까지의 거리
def dfs(v, num):
    num += 1
    visited[v] = 1
    
    if v == target:
        result.append(num)
    
    for i in adj[v]:
        if not visited[i]:
            dfs(i, num)

dfs(beggin, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)
```

### 풀이
- 시작 부분을 기점으로 탐색 시작
- num에 1씩 더하면서 탐색
- target에 도달하면 1을 빼고 최단거리를 출력하거나 num이 result에 저장되지 않는 경우 -1을 출력

```
7 1
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
2 2
[0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
1 3
[0, 1, 1, 0, 0, 0, 0, 1, 0, 0]
3 4
[0, 1, 1, 1, 0, 0, 0, 1, 0, 0]
3 [4]
8 3
[0, 1, 1, 1, 0, 0, 0, 1, 1, 0]
9 3
[0, 1, 1, 1, 0, 0, 0, 1, 1, 1]
3
```