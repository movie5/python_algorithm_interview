### 코드
```
n, m = int(input()), int(input())
adj = {}
for _ in range(m):
    friendship = list(map(int, input().split(' ')))
    for i in friendship:
        if i not in adj:
            adj[i] = []

    for i in range(len(friendship)):
            adj[friendship[i]].append(friendship[(i+1) % len(friendship)])

invite = adj[1].copy()
for i in adj[1]:
    invite.extend(adj[i])

print(len(set(invite)) - 1)
```
### 풀이
- 친구의 친구 까지만 초대하면 됨
- 하지만 친구가 없는 경우를 고려하지 못함
- adj가 dict일 경우 해당 인덱스가 없을 때 KeyError 발생

### 코드
```
n, m = int(input()), int(input())
adj = {1: []}
for _ in range(m):
    friendship = list(map(int, input().split(' ')))
    for i in friendship:
        if i not in adj:
            adj[i] = []

    for i in range(len(friendship)):
            adj[friendship[i]].append(friendship[(i+1) % len(friendship)])

invite = adj[1].copy()
for i in adj[1]:
    invite.extend(adj[i])

if len(set(invite)) == 0:
     print(0)
else:
     print(len(set(invite))-1)
```

### 풀이
- 친구가 없는 경우를 고려해 먼저 빈 리스트를 만들어주고 시작
- set(친구의 인접 리스트 + 친구의 친구 인접 리스트) - 자기 자신