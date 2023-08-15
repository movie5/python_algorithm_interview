```
pypy3로 제출해야통과함
```
```python
'''
<틀린 풀이>
1. 백트래킹이기때문에 q쓰면 다시 돌아올수 x 오답
'''
import sys
from collections import deque

input = sys.stdin.readline
q= deque()
graph= []

for _ in range(9):
    graph.append(list(map(int, input().strip().split())))


for i in range(9):
    for j in range(9):
        if graph[i][j]==0:
            q.append((i,j))

def check_row(x, a):
    if a in graph[x]:
        return False
    return True

def check_col(x,a):
    for i in range(9):
        if a == graph[i][x]:
            return False
    return True
    
def check_rect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True

def dfs():
    if len(q)==0:
        for i in range(9):
            print(*graph[i])
        exit()
    x,y = q.popleft()

    for i in range(1,10):
        if check_row(x, i) and check_col(y, i) and check_rect(x, y, i):
            graph[x][y]=i
            dfs()
            graph[x][y]=0

dfs()        
'''
<정답 풀이>

'''
import sys
from collections import deque

input = sys.stdin.readline
graph= []
blank = [] 
for _ in range(9):
    graph.append(list(map(int, input().strip().split())))


for i in range(9):
    for j in range(9):
        if graph[i][j]==0:
            blank.append((i,j))

def check_row(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def check_col(x,a):
    for i in range(9):
        if a == graph[i][x]:
            return False
    return True
    
def check_rect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True

def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit()
    x = blank[idx][0]
    y= blank[idx][1]

    for i in range(1,10):
        if check_row(x, i) and check_col(y, i) and check_rect(x, y, i):
            graph[x][y]=i
            #print(x,y,idx)
            dfs(idx+1)
            graph[x][y]=0

dfs(0)        
        
        
        
    
    

        



        
        
    
    

        


