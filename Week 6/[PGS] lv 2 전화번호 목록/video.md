```
def solution(phone_book):
    phone_book = sorted(phone_book) # 정렬

    for i in range(0, len(phone_book)-1):

        if (phone_book[i] in phone_book[i+1]) and (phone_book[i+1].index(phone_book[i]) == 0):
            return False 

    return True
```

### 설명
- 브루트포스로 풀기엔 이중 루프를 사용해야 하므로 비효율적 O(n^2)
- O(n)으로 푸는 방식 채택
- 리스트 루프를 돌며 바로 뒤의 요소만 가지고 비교
- 인덱스를 조회하며 해당 요소가 바로 뒤의 요소의 접두사(인덱스가 0)인 경우를 확인