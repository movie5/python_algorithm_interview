```python
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
q= deque()

def bfs(x):
    while q:
        x= q.popleft()
        arr[x]=-2
        for i in range(len(arr)):
            #방금 삭제한 index를 부모노드로 가지는 자식들 모두 탐색
            if x==arr[i]:
                q.append(i)
q.append(k)
bfs(k)
cnt=0
for i in range(len(arr)):
    #삭제된 노드가 아니면서, 리프노드인 경우
    if arr[i]!= -2 and i not in arr:
        #print(i)
        cnt+=1
print(cnt) 
```
    