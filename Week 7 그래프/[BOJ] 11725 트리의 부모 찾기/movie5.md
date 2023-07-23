BFS로 풀이 - 노드가 깊어지면 DFS는 오래 걸려서 

```py
#BFS는 queue로 구현
from collections import deque
import sys
input=sys.stdin.readline


N=int(input())
visited=[False]*(N+1)
answer=[0]*(N+1)
#2D list로 만들어서 BFS 함
E=[[] for _ in range(N+1)]

for i in range(N-1):
    # 리스트로 index에 해당하는 값 배치
    S,D=map(int,input().split())
    E[S].append(D)
    E[D].append(S)


def bfs(E,v,visited):
    que=deque([v])
    visited[v]=True
    #que로 모든 노드 돌아댕기면서 확인
    while que:
        x=que.popleft()
        for i in E[x]:
            #방문하지 않았다면 answer 위치에 저장, que에 추가
            if not visited[i]:
                answer[i]=x
                que.append(i)
                visited[i]=True
           

            
bfs(E,1,visited)

#첫번째 root 노드가 1이니까 2부터 시작한다. 
for i in range(2,N+1):
        print(answer[i])

```
