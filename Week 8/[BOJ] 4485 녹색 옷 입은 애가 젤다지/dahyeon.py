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
                heapq.heappush(cand,(graph[nx][ny],nx,ny))
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