```python
import sys
import heapq
input = sys.stdin.readline
n = int(input())
q=[]
for _ in range(n):
    idx, start,end = map(int,input().split())
    heapq.heappush(q, (start,end))
s_q=[]
cnt=0
while q:
    q_start, q_end = heapq.heappop(q)
    print(q_start, q_end)
    while s_q and s_q[0]<=q_start:
            heapq.heappop(s_q)
    heapq.heappush(s_q, q_end)
    cnt= max(cnt,len(s_q)) #s_q가 처음에는 비어있는 상태이기때문에
print(cnt)
```