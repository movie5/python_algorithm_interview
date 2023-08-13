```
<접근법>
1. 자기 자신이 깨져있는 경우 바로 다음 계란으로 넘어가기
2. 자기 자신만 빼고 다 꺠져있는 경우 바로 다음 계란으로
3. 1,2번 다 아닌 경우 깨진 계란 개수 세서 return

```
```python
import sys
input = sys.stdin.readline

n = int(input().strip())
answer= []

for _ in range(n):
    answer.append(list(map(int, input().strip().split())))
cnt =0

def dfs(idx):
    global cnt
    if idx==n:
        tmp=0
        for i in range(n):
            if answer[i][0]<=0:
                tmp+=1 
        cnt = max(cnt, tmp)
        return
    #자기 자신이 깨져있는 경우
    if answer[idx][0]<=0:
        dfs(idx+1)
        return
    allbroken = True #자기 빼고 다 깨져있는 경우 체크
    for i in range(n):
        if i==idx: 
            continue
        if answer[i][0]>0:
            allbroken = False
            break
    if allbroken:
        cnt= max(cnt, n-1)
        dfs(idx+1)
        return
    
    #하나씩 다 깨보기 (완탐)
    for t in range(n):
        if t==idx: continue
        if answer[t][0]<=0: continue #꺠려는 달걀이 꺠져있다면
        #때리기
        answer[idx][0] -= answer[t][1]
        answer[t][0] -= answer[idx][1]
        dfs(idx+1)
        #복구
        answer[idx][0] += answer[t][1]
        answer[t][0] += answer[idx][1]    
    
dfs(0)
print(cnt)    
```