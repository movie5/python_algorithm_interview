```python
'''
내가 푼 풀이
'''
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        c= phone_book[i]
        next= phone_book[i+1]
        if c[0] != next[:len(c)][0]: continue
        if c[-1] != next[:len(c)][-1]: continue
        if c==next[:len(c)]: return False 
    return True
'''
정답풀이
'''
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
```