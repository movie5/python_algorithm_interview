5567 결혼식
DFS로 풀이!

```py
import sys
input=sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = []

#graph에 입력값들을 index에 해당하는 위치에 값으로 설정
for _ in range(M):
  x, y = map(int, input().split())  
  graph[x].append(y)
  graph[y].append(x)

# dfs로 풀이
def dfs(v, count):
  #깊이가 깊어질 때마다 추가
  count += 1
  visited[v] = True
  #구해야하는 촌수의 사람이 나오면 answer
  if v == B:
    answer.append(count)
  for i in graph[v]:
    if not visited[i]:
      dfs(i, count)

dfs(A, 0)

#촌수가 없으면 -1을 내자
if len(answer) == 0:
  print(-1)
#촌수는 -1 해서
else:
  print(answer[0]-1)

```
