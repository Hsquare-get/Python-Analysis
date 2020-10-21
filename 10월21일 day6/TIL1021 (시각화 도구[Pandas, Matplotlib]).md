# TIL1021 (시각화 도구[Pandas, Matplotlib])

## (1) <span style="color:red;">Pandas 내장 그래프 도구 활용</span>

> 판다스는 Matplotlib 라이브러리의 기능을 일부 내장하고 있어서, 별도로 import 없이도 간단한 그래프를 그릴 수 있다. Series, DataFrame 객체에 plot() 메서드를 적용하여 그래프를 그리며 kind 옵션으로 그래프의 종류를 선택할 수 있다.

- `series.plot(kind)` `df.plot(kind)`

| kind option                                      | Description          |
| ------------------------------------------------ | -------------------- |
| df.plot(kind='**line**') = df.plot()             | 선 그래프            |
| df.plot(kind='**bar**')                          | 수직 막대 그래프     |
| df.plot(kind='**barh**')                         | 수평 막대 그래프     |
| df.plot(kind='**his**')                          | 히스토그램           |
| df.plot(kind='**box**')                          | 박스 플롯            |
| df.plot(kind='**kde**')                          | 커널 밀도 그래프     |
| df.plot(kind='**area**')                         | 면적 그래프          |
| df.plot(kind='**pie**')                          | 파이 그래프          |
| df.plot(kind='**scatter**', x='weight', y='mpg') | 산점도 그래프        |
| df.plot(kind='**hexbin**')                       | 고밀도 산점도 그래프 |

```python
import pandas as pd

# 폰트 오류 해결
from matplotlib import font_manager, rc
font_path = "../data/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

data = {'name':['둘리', '또치', '도우너', '희동이'],
        '국어':[90, 80, 70, 70],
        '영어':[99, 98, 97, 46],
        '수학':[90, 70, 70, 60]}
df = pd.DataFrame(data)
df.set_index('name', inplace=True)

# 선그래프
df.plot(kind='line') # df.plot()

# 막대그래프
df.plot(kind='bar')
df.plot(kind='bar', stacked=True, rot=0)

# 히스토그램 (변수가 하나인 데이터의 빈도수 그래프)
df.plot(kind='hist')

# 수평 막대그래프
df.plot(kind='barh')

# 파이그래프
df.plot(kind='pie', y='국어')

# 산점도
df = pd.read_csv('../data/auto-mpg.csv', header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
df.plot(x='weight',y='mpg', kind='scatter')

# 박스플롯
df[['mpg','cylinders']].plot(kind='box')
```



## (2) <span style="color:red;">Matplotlib</span> & NumPy

> **Matplotlib** : 파이썬 표준 시각화도구
>
> **NumPy** : 행렬이나 대규모 다차원 배열을 쉽게 처리하도록 지원하는 파이썬 라이브러리, 데이터 구조 외에도 계산과학 분야에 효율적으로 구현된 기능을 제공한다

- Matplotlib 한글 폰트 오류 해결

```python
# font 인식 못할 때
# import matplotlib.font_manager as fm 
# fm._rebuild()

from matplotlib import font_manager, rc
font_path = "../data/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
```

- 막대그래프 color

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

series = pd.Series([5, 4, 7, 1, 12],index = ["둘리", "또치", "도우너", "희동이", "마이콜"])

plt.title("시리즈 데이터로 그리는 그래프")
plt.ylabel('갯수')
plt.xlabel('학생이름')

# Set tick colors:
ax = plt.gca() # Axis 축 객체 반환
ax.tick_params(axis='x', colors='blue')
ax.tick_params(axis='y', colors='red')

mycolors = sns.color_palette('Spectral', 5)
plt.bar(x=series.index, height=series, color=mycolors)
plt.show()
```

![막대그래프 color](https://user-images.githubusercontent.com/64063767/96734027-11b63080-13f5-11eb-9758-b99dad9a43c1.png)

---

- **subplot**

```python
import matplotlib.pyplot as plt

# subplot 레이아웃 영역
t = np.arange(0,5, 0.01)

plt.figure(figsize=(10,12))

plt.subplot(4,1,1)
plt.plot(t, np.sqrt(t))
plt.grid(True)

plt.subplot(4,2,3)
plt.plot(t, t**2)
plt.grid(True)

plt.subplot(4,2,4)
plt.plot(t, t**3)
plt.grid(True)

plt.subplot(4,1,3)
plt.plot(t, np.sin(t))
plt.grid(True)

plt.subplot(4,1,4)
plt.plot(t, np.cos(t))
plt.grid(True)

plt.show()
```

![subplot](https://user-images.githubusercontent.com/64063767/96719666-a8c6bc80-13e4-11eb-85b1-e85dc7a911de.png)

---

- **subplots**

```python
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-3,3,100)
y1=np.sin(x)
y2=np.cos(x)
y3=1/(1+np.exp(-x))
y4=np.exp(x)

# fig, ax = plt.subplots(2, 2) # 2개 객체 반환
# constrained_layout=True : 레이아웃 겹치지 않게
fig, ax = plt.subplots(2, 2, constrained_layout=True) 

ax[0,0].plot(x,y1)
ax[0,1].plot(x,y2)
ax[1,0].plot(x,y3)
ax[1,1].plot(x,y4)

ax[0,0].set_title("Sine function")
ax[0,1].set_title("Cosine function")
ax[1,0].set_title("Sigmoid function")
ax[1,1].set_title("Exponential function")

plt.show()
```

![subplot2](https://user-images.githubusercontent.com/64063767/96720067-44582d00-13e5-11eb-9541-945dae3cfb16.png)

---

- **그래프에 글자, 포인터 삽입**

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.cos(x)

fig, axes = plt.subplots(1,2)
axes[0].scatter(x, y, marker=".")
axes[0].text(2,0, "Example Graph", style="italic", size=15)

axes[1].scatter(x, y, marker="*")
axes[1].annotate("Cosine", xy=(5,0.5), xytext=(2,0.75),
                 arrowprops=dict(arrowstyle="simple"))
plt.show()
```

![insertpointer](https://user-images.githubusercontent.com/64063767/96720905-5b4b4f00-13e6-11eb-87ed-5487cdbce0fd.png)

---

- **Sine & Cosine**

```python
import matplotlib.pyplot as plt
import numpy as np

# Sine & Cosine
np.set_printoptions(formatter={'float_kind': lambda x: "{0:0.2f}".format(x)})
t = np.arange(0,12,0.01) # END 포함 X

plt.figure(figsize=(10,6))
plt.plot(t, np.sin(t), label='sin')
plt.plot(t, np.cos(t), label='cos')
plt.grid()
plt.legend() # 각 plot에 label이 있어야 범례(legend)를 나타낼 수 있다
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.xlim(0, 2*np.pi)
plt.ylim(-1.5, 1.5)
plt.show()
```

![Sine,Cosine](https://user-images.githubusercontent.com/64063767/96733611-9d7b8d00-13f4-11eb-816d-4013a3f3a996.png)

---

```python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6] 
y = [1, 4, 5, 8, 9, 5, 3]

plt.figure(figsize=(10,6))
plt.plot(x, y, color='red', linestyle='dashed', 
         marker='o', markerfacecolor='blue', markersize=10) 
# plt.plot(x, y, 'ro--')
plt.show()
```

![기본플롯](https://user-images.githubusercontent.com/64063767/96733471-745afc80-13f4-11eb-8b1c-749453d69251.png)

---

```python
import matplotlib.pyplot as plt
import numpy as np

# 평균(loc), 표준편차(scale), 숫자개수(size)
s1 = np.random.normal(loc=0, scale=1, size=1000)
s2 = np.random.normal(loc=5, scale=0.5, size=1000)
s3 = np.random.normal(loc=10, scale=2, size=1000)

plt.figure(figsize=(10,6))
plt.boxplot((s1, s2, s3), labels=['평균 0', '평균 5', '평균 10'])
plt.grid()
plt.show()
```

![범례 박스플롯](https://user-images.githubusercontent.com/64063767/96732339-301b2c80-13f3-11eb-9c30-516ea848f0b1.png)

---

- **서울 -> 경기 전출 선그래프**

```python
import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "../data/malgun.ttf"   #폰트파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# Excel 데이터를 데이터프레임 변환 
df = pd.read_excel('../data/시도별 전출입 인구수.xlsx', header=0)

# 전출지별에서 누락값(NaN)을 앞 데이터로 채움 (엑셀 양식 병합 부분)
df = df.fillna(method='ffill')

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시') 
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

# 서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']

# 스타일 서식 지정
plt.style.use('ggplot') 

# 그림 사이즈 늘리기
plt.figure(figsize=(14, 5))

# x축 눈금 라벨 회전하기
plt.xticks(size=10, rotation='vertical')

# x, y축 데이터를 plot 함수에 입력 
plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10)  # 마커 표시 추가

plt.title('서울 -> 경기 인구 이동', size=30)  #차트 제목
plt.xlabel('기간', size=20)                  #x축 이름
plt.ylabel('이동 인구수', size=20)           #y축 이름

#범례 표시
plt.legend(labels=['서울 -> 경기'], loc='best', fontsize=15)

# y축 범위 지정 (최소값, 최대값)
plt.ylim(50000, 800000)

# 주석 표시 - 화살표
plt.annotate('',
             xy=(20, 620000),       #화살표의 머리 부분(끝점)
             xytext=(2, 290000),    #화살표의 꼬리 부분(시작점)
             xycoords='data',       #좌표체계
             arrowprops=dict(arrowstyle='->', color='skyblue', lw=5), #화살표 서식
             )

plt.annotate('',
             xy=(47, 450000),       #화살표의 머리 부분(끝점)
             xytext=(30, 580000),   #화살표의 꼬리 부분(시작점)
             xycoords='data',       #좌표체계
             arrowprops=dict(arrowstyle='->', color='olive', lw=5),  #화살표 서식
             )

# 주석 표시 - 텍스트
plt.annotate('인구이동 증가(1970-1995)',  #텍스트 입력
             xy=(10, 550000),            #텍스트 위치 기준점
             rotation=25,                #텍스트 회전각도
             va='baseline',              #텍스트 상하 정렬
             ha='center',                #텍스트 좌우 정렬
             fontsize=15,                #텍스트 크기
             )

plt.annotate('인구이동 감소(1995-2017)',  #텍스트 입력
             xy=(40, 560000),            #텍스트 위치 기준점
             rotation=-11,               #텍스트 회전각도
             va='baseline',              #텍스트 상하 정렬
             ha='center',                #텍스트 좌우 정렬
             fontsize=15,                #텍스트 크기
             )

plt.show() # 변경사항 저장하고 그래프 출력
```

![서울경기](https://user-images.githubusercontent.com/64063767/96726701-33131e80-13ed-11eb-9bfa-5869a400007b.png)

---

- **도시별 전출 추이 그래프**

```python
import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "../data/malgun.ttf"   #폰트파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# Excel 데이터를 데이터프레임 변환 
df = pd.read_excel('../data/시도별 전출입 인구수.xlsx', header=0)

# 전출지별에서 누락값(NaN)을 앞 데이터로 채움 (엑셀 양식 병합 부분)
df = df.fillna(method='ffill')

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시') 
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

# 서울에서 '충청남도','경상북도', '강원도'로 이동한 인구 데이터 값만 선택
col_years = list(map(str, range(1970, 2018)))
df_3 = df_seoul.loc[['충청남도','경상북도', '강원도'], col_years]

# 스타일 서식 지정
plt.style.use('ggplot') 

# 그래프 객체 생성 (figure에 1개의 서브 플롯을 생성)
fig = plt.figure(figsize=(20, 5))   
ax = fig.add_subplot(1, 1, 1) # 하나의 영역에 여러 그래프 그리기

# axe 객체에 plot 함수로 그래프 출력
ax.plot(col_years, df_3.loc['충청남도',:], marker='o', markerfacecolor='green', 
        markersize=10, color='olive', linewidth=2, label='서울 -> 충남')
ax.plot(col_years, df_3.loc['경상북도',:], marker='o', markerfacecolor='blue', 
        markersize=10, color='skyblue', linewidth=2, label='서울 -> 경북')
ax.plot(col_years, df_3.loc['강원도',:], marker='o', markerfacecolor='red', 
        markersize=10, color='magenta', linewidth=2, label='서울 -> 강원')

# 범례 표시
ax.legend(loc='best')

# 차트 제목 추가
ax.set_title('서울 -> 충남, 경북, 강원 인구 이동', size=20)

# 축이름 추가
ax.set_xlabel('기간', size=12)
ax.set_ylabel('이동 인구수', size = 12)

# 축 눈금 라벨 지정 및 90도 회전
ax.set_xticklabels(col_years, rotation=90)

# 축 눈금 라벨 크기
ax.tick_params(axis="x", labelsize=10)
ax.tick_params(axis="y", labelsize=10)

plt.show() # 변경사항 저장하고 그래프 출력
```

![서울충남경북강원](https://user-images.githubusercontent.com/64063767/96727053-9a30d300-13ed-11eb-833a-0bd7c96fb2c1.png)

---

- **도시별 전출인원 면적그래프**

```python
import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "../data/malgun.ttf"   #폰트파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# Excel 데이터를 데이터프레임 변환
df = pd.read_excel('../data/시도별 전출입 인구수.xlsx', header=0)

# 전출지별에서 누락값(NaN)을 앞 데이터로 채움 (엑셀 양식 병합 부분)
df = df.fillna(method='ffill')

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시') 
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

# 서울에서 '충청남도','경상북도', '강원도', '전라남도'로 이동한 인구 데이터 값만 선택
col_years = list(map(str, range(1970, 2018)))
df_4 = df_seoul.loc[['충청남도','경상북도', '강원도', '전라남도'], col_years]
df_4 = df_4.transpose()

# 스타일 서식 지정
plt.style.use('ggplot') 

# 데이터프레임의 인덱스를 정수형으로 변경 (x축 눈금 라벨 표시)
df_4.index = df_4.index.map(int)

# 면적 그래프 그리기
df_4.plot(kind='area', stacked=True, alpha=0.2, figsize=(20, 10))

plt.title('서울 -> 타시도 인구 이동', size=30)
plt.ylabel('이동 인구 수', size=20)
plt.xlabel('기간', size=20)
plt.legend(loc='best', fontsize=15)

plt.show()
```

![도시별전출면적그래프](https://user-images.githubusercontent.com/64063767/96727467-090e2c00-13ee-11eb-9f09-b53144319143.png)

---

- **도시별 전출인원 막대그래프**

```python
import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "../data/malgun.ttf"   #폰트파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# Excel 데이터를 데이터프레임 변환
df = pd.read_excel('../data/시도별 전출입 인구수.xlsx', header=0)

# 전출지별에서 누락값(NaN)을 앞 데이터로 채움 (엑셀 양식 병합 부분)
df = df.fillna(method='ffill')

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시') 
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

# 서울에서 '충청남도','경상북도', '강원도', '전라남도'로 이동한 인구 데이터 값만 선택
col_years = list(map(str, range(2010, 2018)))     
df_4 = df_seoul.loc[['충청남도','경상북도', '강원도', '전라남도'], col_years]
df_4 = df_4.transpose()

# 스타일 서식 지정
plt.style.use('ggplot') 

# 데이터프레임의 인덱스를 정수형으로 변경 (x축 눈금 라벨 표시)
df_4.index = df_4.index.map(int)

# 막대 그래프 그리기
df_4.plot(kind='bar', figsize=(20, 10), width=0.7,
          color=['orange', 'green', 'skyblue', 'blue'])

plt.title('서울 -> 타시도 인구 이동', size=30)
plt.ylabel('이동 인구 수', size=20)
plt.xlabel('기간', size=20)
plt.ylim(5000, 30000)
plt.legend(loc='best', fontsize=15)

plt.show()
```

![도시별전출막대그래프](https://user-images.githubusercontent.com/64063767/96728188-d1ec4a80-13ee-11eb-8709-6c04c04d45a2.png)

---

- **2축 그래프(보조축)** 

```python
import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "../data/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# Excel 데이터를 데이터프레임 변환
df = pd.read_excel('../data/남북한발전전력량.xlsx', convert_float=True)
df = df.loc[5:9]
df.drop('전력량 (억㎾h)', axis='columns', inplace=True)
df.set_index('발전 전력별', inplace=True)
df = df.T 

# 증감율(변동률) 계산
df = df.rename(columns={'합계':'총발전량'})
df['총발전량 - 1년'] = df['총발전량'].shift(1)
df['증감율'] = ((df['총발전량'] / df['총발전량 - 1년']) - 1) * 100      

# 2축 그래프 그리기
ax1 = df[['수력','화력']].plot(kind='bar', figsize=(20, 10), width=0.7, stacked=True)  
ax2 = ax1.twinx()
ax2.plot(df.index, df.증감율, ls='--', marker='o', markersize=20, 
         color='green', label='전년대비 증감율(%)')  

ax1.set_ylim(0, 500)
ax2.set_ylim(-50, 50)

ax1.set_xlabel('연도', size=20)
ax1.set_ylabel('발전량(억 KWh)')
ax2.set_ylabel('전년 대비 증감율(%)')

plt.style.use('ggplot')   # 스타일 서식 지정
plt.rcParams['axes.unicode_minus']=False   # 마이너스 부호 출력 설정
plt.title('북한 전력 발전량 (1990 ~ 2016)', size=30)
ax1.legend(loc='upper left')

plt.show()
```

![2축그래프](https://user-images.githubusercontent.com/64063767/96729316-fac10f80-13ef-11eb-85ac-97e127caf433.png)

---

- **산점도 버블차트**

```python
import pandas as pd
import matplotlib.pyplot as plt

# CSV 데이터를 데이터프레임 변환
df = pd.read_csv('../data/auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# cylinders 개수의 상대적 비율을 계산하여 시리즈 생성
cylinders_size = df.cylinders / df.cylinders.max() * 300

# 3개의 변수로 산점도 그리기 
plt.style.use('default') # 스타일 서식 지정
df.plot(kind='scatter', x='weight', y='mpg', c='coral', figsize=(10, 5),
        s=cylinders_size, alpha=0.3) # alpha(투명도)
plt.title('Scatter Plot: mpg-weight-cylinders')
plt.show()
```

![산점도 버블차트](https://user-images.githubusercontent.com/64063767/96729909-9e122480-13f0-11eb-9d2d-53f957363643.png)

---

- **파이 차트**

```python
import pandas as pd
import matplotlib.pyplot as plt

# CSV 데이터를 데이터프레임 변환
df = pd.read_csv('../data/auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 데이터 개수 카운트를 위해 값 1을 가진 열을 추가
df['count'] = 1
df_origin = df.groupby('origin').sum()   # origin 열을 기준으로 그룹화, 합계 연산

# 제조국가(origin) 값을 실제 지역명으로 변경
df_origin.index = ['USA', 'EU', 'JAPAN']

# 제조국가(origin) 열에 대한 파이 차트 그리기 – count 열 데이터 사용
df_origin['count'].plot(kind='pie', 
                     figsize=(7, 5),
                     autopct='%1.1f%%',   # 퍼센트 % 표시
                     startangle=10,       # 파이 조각을 나누는 시작점(각도 표시)
                     colors=['chocolate', 'bisque', 'cadetblue']    # 색상 리스트
                     )

plt.style.use('default') # 스타일 서식 지정
plt.title('Model Origin', size=20)
plt.axis('equal')    # 파이 차트의 비율을 같게 (원에 가깝게) 조정
plt.legend(labels=df_origin.index, loc='upper right')   # 범례 표시
plt.show()
```

![파이차트](https://user-images.githubusercontent.com/64063767/96730486-298bb580-13f1-11eb-8a87-bd7456802327.png)

