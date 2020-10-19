# TIL1019 (Pandas Library)


## (1) <span style="color:red;">pandas library</span>

> 판다스 라이브러리는 데이터를 수집하고 정리하는 데 최적화된 도구이며 통계와 데이터과학, 머신러닝 분야에서 이용되는 소프트웨어이다.

- 판다스는 **시리즈(Series)**와 **데이터프레임(DataFrame)**이라는 구조화된 데이터 형식을 제공



### (I) 시리즈(Series)

- 시리즈는 데이터가 순차적으로 나열된 **1차원 배열**의 형태를 갖는다.
- 인덱스(index)는 데이터 값(value)과 일대일 대응이 되어 **딕셔너리와 비슷한 구조**를 갖는다.

- R의 Vector와 유사하지만 **다양한 자료형을 담을 수 있다**는 것이 큰 차이점이다.

```python
import pandas as pd

# k:v 구조를 갖는 딕셔너리를 만들고, 변수 dict_data에 저장
dict_data = {'a': 1, 'b': 2, 'c': 3}

# 판다스 Series() 함수로 딕셔너리(dict_data)를 시리즈로 변환
series = pd.Series(dict_data)

# 인덱스 배열은 변수 idx에 저장. 데이터 값 배열은 변수 val에 저장
idx = series.index # Index(['a', 'b', 'c'], dtype='object')
val = series.values # [1 2 3]

# 튜플을 시리즈로 변환(index 옵션에 인덱스 이름을 지정)
tup_data = ('영인', '2010-05-01', '여', True)
series = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])

# 원소를 1개 선택
print(series[0])      # series의 1 번째 원소를 선택 (정수형 위치 인덱스를 활용)
print(series['이름'])  # '이름' 라벨을 가진 원소를 선택 (인덱스 이름을 활용)

# 여러 개의 원소를 선택 (인덱스 리스트 활용)
print(series[[1, 2]])
print(series[['생년월일', '성별']])

# 여러 개의 원소를 선택 (인덱스 범위 지정)
print(series[1 : 2]) # 숫자 인덱스는 END 포함 X
print(series['생년월일' : '성별']) # 이름 인덱스는 END 포함
```



### (II) 데이터프레임(DataFrame)

- 데이터프레임은 **2차원 배열**이다.
- 데이터프레임의 **열은 각각의 시리즈 객체**이다.

```python
import pandas as pd

# 열이름을 key로 하고, 리스트를 value로 갖는 딕셔너리 정의(2차원 배열)
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 판다스 DataFrame() 함수로 딕셔너리를 데이터프레임으로 변환
df = pd.DataFrame(dict_data)

# 행 인덱스 / 열 이름 지정하여, 데이터프레임 만들기
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], 
                   index=['준서', '예은'],
                   columns=['나이', '성별', '학교'])


# 행 인덱스, 열 이름 확인하기
print(df.index)      # Index(['준서', '예은'], dtype='object')
print(df.columns)    # Index(['나이', '성별', '학교'], dtype='object')

# 열 이름 중, '나이'를 '연령'으로, '성별'을 '남녀'로, '학교'를 '소속'으로 바꾸기
# (바꾸고 싶은 열 이름만 바꿀 수 있다)
a = df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace=True) 
# inplace = True --> df 원본을 변경
# inplace = False --> df 원본을 복제하여 객체를 생성

# df의 행 인덱스 중에서, '준서'를 '학생1'로, '예은'을 '학생2'로 바꾸기
# (바꾸고 싶은 행 이름만 바꿀 수 있다)
df.rename(index={'준서':'학생1', '예은':'학생2' }, inplace=True)


# 행과 열 삭제
exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
df2 = df.copy()
df2.drop(['우현', '인아'], axis=0, inplace=True) # 행 삭제, axis=0(default)
df3 = df.copy()
df3.drop(['영어', '음악'], axis=1, inplace=True) # 열 삭제, axis=1 필수


# 행 인덱스를 사용하여 행 1개를 선택
df.loc['서준']
df.iloc[0]

# 행 인덱스를 사용하여 2개 이상의 행 선택
df.loc[['서준', '우현']]
df.iloc[[0, 1]]

# 행 인덱스의 범위를 지정하여 행 선택
df.loc['서준':'우현'] # loc 인덱서 : 인덱스 이름 (숫자도 가능, END 포함)
df.iloc[0:1]         # iloc 인덱서 : 숫자 인덱스 (END 포함 X)
df.iloc[::2]
df.iloc[::-1]

# 1개의 열 선택
df['수학']
df[['수학']] # 하나의 열만 선택했지만 데이터프레임 유지
df.영어      # 열 이름이 문자열일 경우에만 가능

# 2개 이상의 열 선택
df[['음악', '체육']]

# 특정 '이름' 열을 새로운 인덱스로 지정하고, df 객체에 변경사항 반영
df.set_index('이름', inplace=True)

# 데이터프레임 df의 특정 원소 1개 선택 ('서준'의 '음악' 점수)
df.loc['서준', '음악']
df.iloc[0, 2] # 0행 2열('서준'의 '음악' 점수)

# 데이터프레임 df의 특정 원소 2개 이상 선택 ('서준'의 '음악', '체육' 점수) 
df.loc['서준', ['음악', '체육']]
df.iloc[0, [2, 3]]
df.loc['서준', '음악':'체육']

# df의 2개 이상의 행과 열로부터 원소 선택 ('서준', '우현'의 '음악', '체육' 점수) 
df.loc[['서준', '우현'], ['음악', '체육']]
df.iloc[[0, 1], [2, 3]]
df.loc['서준':'우현', '음악':'체육']


# 데이터프레임 df에 '국어' 점수 열(column)을 추가. 데이터 값은 80 지정
df['국어'] = 80
df.국어 = [100, 90, 80]
df.사회 = 70 # 적용안됨, 처음 추가하는 열이름인 경우에는 . 사용 못함

# 새로운 행(row)을 추가 - 같은 원소 값을 입력
df.loc[3] = 0

# 새로운 행(row)을 추가 - 원소 값 여러 개의 배열 입력
df.loc[4] = ['동규', 90, 80, 70, 60]


# 데이터프레임 df의 특정 원소를 변경하는 방법: '서준'의 '체육' 점수
df.iloc[0][3] = 80
df.loc['서준']['체육'] = 90

# 데이터프레임 df의 원소 여러 개를 변경하는 방법: '서준'의 '음악', '체육' 점수
df.loc['서준', ['음악', '체육']] = 50


# 데이터프레임 df를 전치하기
df = df.transpose() # (메소드 활용)
df = df.T # (클래스 속성 활용)
```



- 인덱스(행) 활용

```python
import pandas as pd

# 딕셔서리를 정의
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 딕셔서리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r2]로 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])

# 인덱스를 [r0, r1, r2, r3, r4]로 재지정
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index, fill_value=0) # reindex로 발생한 NaN값을 숫자 0으로 채우기

# 행 인덱스를 정수형으로 초기화 
ndf = df.reset_index()

# 내림차순으로 행 인덱스 정렬 
ndf = df.sort_index(ascending=False)

# c1 열을 기준으로 내림차순 정렬 
ndf = df.sort_values(by='c1', ascending=False)
```



- 산술연산

> 판다스 객체의 산술연산은 내부적으로 3단계 프로세스를 거친다.
>
> 1. 행/열 인덱스를 기준으로 모든 원소를 정렬한다
> 2. 동일한 위치에 있는 원소끼리 일대일로 대응시킨다
> 3. 일대일 대응이 되는 원소끼리 연산을 처리한다 (이 때 **대응되는 원소가 없으면 NaN 처리**)

```python
import pandas as pd

# 딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90, '영어':80})

addition = student1 + student2               #덧셈
subtraction = student1 - student2            #뺄셈
multiplication = student1 * student2         #곱셈
division = student1 / student2               #나눗셈

# 사칙연산 결과를 데이터프레임으로 합치기 (시리즈 -> 데이터프레임)
result = pd.DataFrame([addition, subtraction, multiplication, division], 
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
```



```python
import pandas as pd

# 딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})

# 두 학생의 과목별 점수로 사칙연산 수행 (연산 메소드 사용)
sr_add = student1.add(student2, fill_value=0)    #덧셈
sr_sub = student1.sub(student2, fill_value=0)    #뺄셈
sr_mul = student1.mul(student2, fill_value=0)    #곱셈
sr_div = student1.div(student2, fill_value=0)    #나눗셈

# 사칙연산 결과를 데이터프레임으로 합치기 (시리즈 -> 데이터프레임)
result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div], 
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
```

