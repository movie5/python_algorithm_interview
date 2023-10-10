# 에러
- 런타임 에러 (TypeError) 발생
```
import sys
input = sys.stdin.readline()
```
- 	런타임 에러 (SyntaxError) 발생
```
result = 0
a = input().split("-")
for i in a[0].split("+"):
    result += int(eval(i))
for i in a[1:]:
    for j in i.split("+"):
        result -= int(eval(j))

print(result)
```
# 정답
```
a = input().split("-")
result = 0

for i in a[0].split("+"):
    result += int(i)

for i in a[1:]:
    for j in i.split("+"):
        result -= int(j)

print(result)
```