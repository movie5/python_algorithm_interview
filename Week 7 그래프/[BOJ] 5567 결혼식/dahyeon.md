```
메모리 : 39804kb
시간 : 224ms
```
```python
import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

n = int(input())
m = int(input())

q= deque()
#1에서부터 시작하므로 (n+1)개 해야함.
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

#그래프 생성
for i in range(m):
    a,b = map(int,input().strip().split())

    graph[a].append(b)
    graph[b].append(a)


#그래프 탐색
def dfs():
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i]==0:
                visited[i]=visited[a]+1
                q.append(i)
q.append(1)
visited[1]=1
dfs()

result=0
#완탐해서 찾기
for i in range(2,n+1):
    if visited[i]<=3 and visited[i]!=0: #한번도 방문안하는 것있을수도있으므로
        result+=1
print(result) 
```