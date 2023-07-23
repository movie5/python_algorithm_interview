# 32번 문제

## DFS 재귀

1. 동서남북이 연결된 그래프로 가정하고, 네개의 방향 DFS 재귀 탐색을 마치면 1이 증가

```py
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == '1':
      self.dfs(grid, i, j)
```

행, 열 단위로 육지(1)인 곳을 찾아 진행하다가 발견하면 self.dfs()를 호출한다

```py
def dfs(self, grid, i, j):
  # 더이상 땅이 아닌 경우 종료, 방문했던 곳은 1이 아닌 값으로 마킹
  if i < 0 or i >= len(grid) or  j <0 or j >= len(grid[0]) or grid[i][j] != '1':
    return

  grid[i][j] = '0'

  #동서남북 탐색
  self.dfs(grid, i+1, j)
  self.dfs(grid, i-1, j)
  self.dfs(grid, i, j+1)
  self.dfs(grid, i, j-1)
```

백트래킹으로 모두 빠져 나오면 섬 하나를 발견한 것으로 간주한다. 

별도의 행렬을 생성할 경우 시간 복잡도가 *O(n)* 이 된다.

dfs() 함수를 빠져나오면 해당 위치에서 탐색할 수 있는 모든 육지를 탐색한 것이 된다. 카운트를 1 증가시킨다. 

예외 처리는 if not grid: return 0으로 한다. 그리고 위의 함수대로 하면 매번 호출이 일어나게 되서 class의 멤버 변수로 변경할 수 있다. 

```py
Class Solution:
  grid : List[List[str]
  def ...
  def ...
```

그러나 이렇게 작성해도 클래느 내에서 멤버 변수로 선언해서 공유하여 grid를 매번 넘기지 않을 수 있지만, 함수 호출 시 self가 따라오게 된다. 
그래서 중첩함수로 사용해서 함수 안에 함수를 만들어 보낼 수 있다. 
