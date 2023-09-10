```
<접근법>
1. 도둑루피를 가중치로 생각하고 다익스트라 알고리즘
```
```python
'''
틀린 풀이
=> 4방향중 가장 작은 도둑루피로 가는 쪽으로
'''
from collections import deque
import sys
from pprint import pprint
import heapq
input = sys.stdin.readline
def main(n):
    graph = []
    q = deque()
    dx=[-1,1,0,0]
    dy= [0,0,-1,1]
    for i in range(n):
        graph.append(list(map(int, input().split())))
    visited = [[0]*n for _ in range(n)]
    q.append((0,0))
    answer=0
    visited[0][0]=1
    while q:
        #print(visited)
        x,y= q.popleft()
        cand= []
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                cand.append(graph[nx][ny],nx,ny)
                visited[nx][ny]=1
        try:
            dis, nx,ny = heapq.heappop(cand)
            answer+= dis
            q.append((nx,ny))
        except:
            pass
    print(answer)
while True:
    n = int(input())
    if n==0:
        exit()
    main(n)

'''
정답풀이
'''
from collections import deque
import sys
from pprint import pprint
import heapq
input = sys.stdin.readline
def main(n):
    graph = []
    q = []
    dx=[-1,1,0,0]
    dy= [0,0,-1,1]
    INF = sys.maxsize
    for i in range(n):
        graph.append(list(map(int, input().split())))
    visited = [[INF]*n for _ in range(n)]
    heapq.heappush(q, (graph[0][0],0,0))
    visited[0][0]=0
    while q:
        #pprint(visited)
        cost, x,y= heapq.heappop(q)
        if x == n - 1 and y == n - 1:
            print(f'Problem {count}: {visited[x][y]}')
            break
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                new_cost = cost+graph[nx][ny]
                if new_cost < visited[nx][ny]:
                    visited[nx][ny]=new_cost
                    heapq.heappush(q,(new_cost, nx,ny))
count=1
while True:
    n = int(input())
    if n==0:
        exit()
    main(n)
    count+=1
```