```
<접근법>
1. A노드에서 root 노드로 가는 경로를 저장할 set을 선언
(if B in set 에서 set의 시간복잡도가 O(1)이기 때문에)

2. A에서 루트에 닿을때까지 경로저장

3. B에서 루트에 닿는 도중에 경로와 겹치는 부분이 있다면 출력 후 종료
```
```python
import sys
from collections import deque
input = sys.stdin.readline
q= deque()

t = int(input().strip())
for _ in range(t):
    n= int(input().strip())
    #한방향으로만 graph만들면됨.
    graph = [0 for _ in range(n+1)]

    for i in range(n-1):
        a,b = map(int, input().strip().split())
        graph[b]= a #graph[a]=b 아니게 조심! 자식노드을 key값으로 부모노드를 꺼내야함
    A,B = map(int, input().split())
    parent_list = set({})
    while A!=0: #루트노드까지
        parent_list.add(A)
        A=graph[A]
    while True: #루트노드에선 A와 B가 반드시 만나므로 while문 종료가 보장된다.
        if B in parent_list:
            print(B)
            break
        B= graph[B]
```