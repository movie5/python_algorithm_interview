```python
def solution(n, arr1, arr2):
    answer=[]
    for one, two in zip(arr1,arr2):
        tmp = str(bin(one | two))[2:]
        tmp= tmp.rjust(n,'0')
        tmp =tmp.replace('1','#')
        tmp=tmp.replace('0',' ')
        answer.append(tmp)
    return answer
```