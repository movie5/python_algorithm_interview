```python
numbers = [2,7,11,15]
target=9

right=0
tmp=0
n= len(numbers)

#풀이 1: 두수라는 제한없고, 연속적일때
for left in range(n):
    while right<n and tmp<target:
        tmp+=numbers[right]
        right+=1
    if tmp==target:
        print([left+1,right])
    tmp-=numbers[left]

#풀이2: 두수라는 제한이 있을때
left,right=0,n-1
while not left == right:
    if numbers[left]+numbers[right]<target:
        left+=1
    elif numbers[left]+numbers[right]>target:
        right-=1
    else:
        print([left+1,right+1])
        break
```