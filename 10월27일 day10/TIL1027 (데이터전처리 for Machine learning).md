# TIL1027 (데이터 전처리 for Machine learning)

> Scikit-learn의 ML 알고리즘을 사용하려면 다음과 같은 조건이 만족되는 데이터 셋이 필요하다



#### (i) 결측치(nan, null) 값이 허용되지 않는다

- nan(null) 값이 얼마 없으면 중앙값이나 평균값으로 대체해본다.
- nan(null) 값이 대다수라면 해당 피쳐값을 drop하는 것도 방법이다.
- 중요도가 높은 피쳐는 유지시킨다.



#### (ii) 문자열도 허용되지 않는다

- 문자열이 허용되지 않기 때문에, 해당 피쳐값에 대한 <span style="color:red;">**인코딩(숫자로 변환)이 필요**</span>하다.
- 인코딩은 대부분 카테고리형(코드 값)으로 변환시킨다.
- 필요없는 피쳐는 drop 한다.



### 레이블 인코딩

> 문자열로 구성되어있는 items 데이터를 카테고리화(코드화)하는 작업

```python
from sklearn.preprocessing import LabelEncoder

items=['TV', '냉장고', '전자레인지', '컴퓨터', '선풍기', '선풍기', '믹서', '믹서']
encoder = LabelEncoder()
encoder.fit(items)

labels = encoder.transform(items)
labels
>>> array([0, 1, 4, 5, 3, 3, 2, 2], dtype=int64)
```

```python
encoder.classes_
>>> array(['TV', '냉장고', '믹서', '선풍기', '전자레인지', '컴퓨터'], dtype='<U5')
```

```python
encoder.inverse_transform([4, 5, 2, 0, 1, 1, 3, 3])
>>>
array(['전자레인지', '컴퓨터', '믹서', 'TV', '냉장고', '냉장고', '선풍기', '선풍기'],dtype='<U5')
```

> <주의> 여기서의 숫자들은 숫자로서의 의미가 아닌 단순한 코드의 의미로 사용되는 것이다. 따라서 이 상태로 바로 ML 알고리즘에 적용하면 숫자로 변환된 변수가 가중치에 영향을 줄 수 있으니 별도의 조치를 취해줘야한다.



### 원-핫 인코딩 (One-Hot Encoding)

> One-Hot Encoding은 dummy 변수 개념을 활용하여 새롭게 코드화하는 작업이다.

```python
from sklearn.preprocessing import OneHotEncoder
import numpy as np

items=['TV', '냉장고', '전자레인지', '컴퓨터', '선풍기', '선풍기', '믹서', '믹서']

encoder = LabelEncoder()
encoder.fit(items)

labels = encoder.transform(items)
labels = labels.reshape(-1,1)
print(labels)

oh_encoder = OneHotEncoder()
oh_encoder.fit(labels)
oh_labels = oh_encoder.transform(labels)
print(oh_labels.toarray())
print(oh_labels.shape)

>>>
[[0]
 [1]
 [4]
 [5]
 [3]
 [3]
 [2]
 [2]]
[[1. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 0. 1.]
 [0. 0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0. 0.]
 [0. 0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0.]]
(8, 6)
```



### pandas의 get_dummies 기능을 활용한 인코딩

> One-Hot Encoding으로도 인코딩이 가능하지만, pandas의 get_dummies()를 활용하면 쉽게 변환해준다.

```python
import pandas as pd

df = pd.DataFrame({'item' : ['TV', '냉장고', '전자레인지', '컴퓨터', '선풍기', '선풍기', '믹서', '믹서']})

pd.get_dummies(df)
```

![get_dummies](https://user-images.githubusercontent.com/64063767/97456523-4f2e3700-197c-11eb-860a-838b1c7ff775.png)

---



### 정규화(Normalization) / 표준화(Standardization)

> 데이터 분석을 수행하면서 많이 겪는 문제중 하나가 *데이터 단위의 불일치*이다. 이를 해결하는 방법으로 <span style="color:blue">**Normalization(정규화)**</span>과 <span style="color:blue">**Standardization(표준화)**</span>가 있다. 이 방법들은 대표적으로 2개 이상의 대상이 단위가 다를 때 대상 데이터를 같은 기준으로 볼 수 있게 해준다. 즉, 다른 데이터와 같이 분석을 할 때에도 표준화 또는 정규화된 데이터를 이용하면 단위 차이 문제 등에서 벗어날 수 있다.

- **정규화(Normalization)**

  > 다음과 같은 공식으로 **특성 값의 범위를 [0,1]로 변환**한다.

  <span style="color:red">**(측정값 - 최소값) / (최대값 - 최소값)**</span>

  

- **표준화(Standardization)**

  > 표준화는 데이터를 0중심으로 **양쪽으로 데이터를 분포시키는 방법**이다.
  >
  > 표준화를 하면 각 데이터의 **평균을 기준으로 얼마나 떨어져 있는지**를 나타내는 값으로 변환된다.

  <span style="color:blue">**Z-score 표준화**</span> : <span style="color:red;">**(측정값 - 평균) / 표준편차**</span>