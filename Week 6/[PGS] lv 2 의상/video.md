```
import pandas as pd
    
def solution(clothes):
    clothes_df = pd.DataFrame(clothes, columns=["name", "class"])
    unique_classes = clothes_df.iloc[:, 1].unique()
    hsh = {}
    answer = 1
    for clss in unique_classes:
        hsh[clss] = list(clothes_df[clothes_df["class"] == clss]["name"])
        answer *= len(hsh[clss])+1
    print(hsh)
    return answer-1
```
### 풀이
- 입력 clothes를 데이터프레임으로 변환
- 종류 별로 옷 이름 리스트를 나열하는 딕셔너리 생성
- 해당 의상 종류를 입지 않는 경우 고려하여 옷 가지수에 1을 더해 경우의 수 도출
- 옷을 모두 입지 않는 경우는 없기 때문에 최종 경우의 수에서 1을 뺌