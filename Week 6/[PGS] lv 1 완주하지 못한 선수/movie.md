``` python
# 실패 
import collections
def solution(participant, completion):
    #counter 사용
    count_parti = collections.Counter(participant)
    count_compl = collections.Counter(completion)
    
    for name in count_compl:
        if name in count_parti:
            count_parti[name] -=1
            
    for item in count_parti:
        return item
```
나중에 코드를 보았는데, 빼기가 가능하더군요 
![image](https://github.com/movie5/python_algorithm_interview/assets/43196430/794b26b4-7751-4e51-9b09-9d19b79b50e5)

```python
#성공
def solution(participant, completion):
    freq = {}
    for name in participant:
        if name not in freq:
            freq[name] = 1
        else:
            freq[name] +=1

    for name in completion:
        freq[name] -= 1
        if freq[name] == 0:
            del freq[name]
    for item in freq:
        return item
```
위의 코드로 counter사용하지 않앗더니 통과되었습니다. 
