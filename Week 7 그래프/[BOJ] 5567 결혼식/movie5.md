5567 결혼식
DFS로 풀이!

![image](https://github.com/movie5/python_algorithm_interview/assets/43196430/ab17a45d-cb8f-40f6-9d50-9e6457c7e564)


풀이 출처 : https://nbalance97.tistory.com/200

```py
import sys

# 런타임 에러 발생 https://www.acmicpc.net/board/view/81353
#readline()으로 입력받으면 마지막에 줄 바꿈 문자가 들어와서 rstrip으로 처리해야함
#input 변수를 덮어쓴다음 input 함수를 그대로 사용해줘야한다
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
visited[1] = True

#기존에서 바꾸니까 12ms정도 빨라짐
for _ in range(m):
    p1, p2 = map(int, input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)

# graph, visited 인자 없에니 4ms정도 빨라짐
def dfs(person, depth):
    if depth == 2:
        return
    for nx in graph[person]:
        if not visited[nx]:
            visited[nx] = True
        dfs(nx, depth+1)    

dfs(1, 0)
print(len(list(filter(lambda x:x==True, visited))) - 1)


```
## 문제
![image](https://github.com/movie5/python_algorithm_interview/assets/43196430/dfe0b0ea-8280-4890-a5b4-4086feba376c)

```
input
"""
6
5
1 2
1 3
3 4
2 3
4 5
"""
```

## 확인하고 싶은 코드
```py
#graph에 입력값들을 index에 해당하는 위치에 값으로 설정
for _ in range(M):
  x, y = map(int, input().split())  
  graph[x].append(y)
  graph[y].append(x)
```

### line별 graph 결과

graph = [[] for _ in range(n+1)]
[[], [], [], [], [], [], []]

```py
#1 1 2 입력
[[], [2], [1], [], [], [], []]

#2 1 3 입력 
[[], [2, 3], [1], [1], [], [], []]

#3 3 4 입력 
[[], [2, 3], [1], [1, 4], [3], [], []]

#4 2 3 입력 
[[], [2, 3], [1, 3], [1, 4, 2], [3], [], []]

#5 4 5 입력 
[[], [2, 3], [1, 3], [1, 4, 2], [3, 5], [4], []]
```

#최종 결과

1부터 시작하기 때문에 인덱스 0인 부분은 내용이 없다. 그렇다고 없에면 에러뜬다.

그리고 n+1일로 해서 마지막은 빈 셀로 둔다. 
