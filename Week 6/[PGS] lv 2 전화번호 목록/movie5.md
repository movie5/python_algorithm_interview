```python

def solution(phone_book):
    #문자열로 입력이 주어져서 이미 sorted되어있다. 
    #접두어이기 때문에 in을 쓰면 안된다. 뒤에 겹치는것도 카운트된다...
    #번호를 key로 두면 비교하기 힘들다. 순서:key, 번호 : value로 한다
    num  = list(range(len(phone_book)))
    book = dict(zip(num, phone_book))
    #이렇게해서 book[i]가 key로 바로 변환 가능
    for i in range(len(book)):
        co = len(book[i])
        for j in range(i+1, len(book)):
            if book[i] in book[j][0:co]:
                return False
    return True

```
        
