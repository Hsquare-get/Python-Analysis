# TIL1022 (시각화 도구[Seaborn, Folium])

## (1) <span style="color:red;">Seaborn</span>

> Matplotlib의 기능과 스타일을 확장한 파이썬 고급시각화 라이브러리

| Use               | Description |
| ----------------- | ----------- |
| sns.lineplot()    | 선 그래프   |
| sns.barplot()     | 막대 그래프 |
| sns.boxplot()     | 박스플롯    |
| sns.scatterplot() | 산점도      |
| sns.pairplot()    | 페어플롯    |
| sns.heatmap()     | 히트맵      |

- **산점도** `sns.scatterplot()`

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
sns.scatterplot(x="petal_length", 
                y="petal_width",
                data=iris,
                hue="species") # hue='species' 열의 유니크 데이터별로 color 구분
plt.show()
```

![seaborn_scatterplot](https://user-images.githubusercontent.com/64063767/97006483-e9f0d500-157a-11eb-9cd9-0a194537f014.png)

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

X = np.random.normal(0,1,100)
Y = np.random.normal(0,1,100)
C = np.random.randint(0,5,100)
cmap_lst = [plt.cm.rainbow, plt.cm.Blues, plt.cm.autumn, plt.cm.RdYlGn]

fig, axes = plt.subplots(1, 4, sharex=True, sharey=True)
fig.set_size_inches((16,4)) 
sns.set(style='whitegrid')

for i in range(0, 4):
    axes[i].scatter(X, Y, c=C, cmap=cmap_lst[i]) # matplotlib scatter
    axes[i].set_title("cmap: {}".format(cmap_lst[i].name))
    
# .svg : 이미지이면서도 바이너리가 아닌 XML 텍스트문서 (해상도의 영향을 받지 않는다 -> 회사로고)
plt.savefig('../output/test.svg')
plt.show()
```

![seaborn_scatterplot(colorful)](https://user-images.githubusercontent.com/64063767/97007078-ca0de100-157b-11eb-9c84-c62d86a7f43b.png)

---

- **회귀선이 있는 산점도** `sns.regplot`

```python
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('darkgrid')

# 그래프 객체 생성 (figure에 2개의 서브 플롯을 생성)
fig = plt.figure(figsize=(15,5))   
ax1 = fig.add_subplot(1,2, 1)
ax2 = fig.add_subplot(1,2, 2)
 
# 그래프 그리기 - 선형회귀선 표시(fit_reg=True)
sns.regplot(x='age',        # x축 변수
            y='fare',       # y축 변수
            data=titanic,   # 데이터
            ax=ax1)         # ax 객체 - 1번째 그래프 

# 그래프 그리기 - 선형회귀선 미표시(fit_reg=False)
sns.regplot(x='age',        # x축 변수
            y='fare',       # y축 변수
            data=titanic,   # 데이터
            ax=ax2,         # ax 객체 - 2번째 그래프 
            fit_reg=False)  # 회귀선 미표시

plt.show()
```

![seaborn_regplot](https://user-images.githubusercontent.com/64063767/96999975-0ee04a80-1571-11eb-9f5e-692726710d41.png)

---

- **히스토그램/커널 밀도 그래프** `sns.distplot()`

```python
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('darkgrid')

# 그래프 객체 생성 (figure에 3개의 서브 플롯을 생성)
fig = plt.figure(figsize=(15,5))   
ax1 = fig.add_subplot(1,3, 1)
ax2 = fig.add_subplot(1,3, 2)
ax3 = fig.add_subplot(1,3, 3)
 
# 기본값 (히스토그램 + 커널밀도그래프)
sns.distplot(titanic['fare'], ax=ax1) 

# hist=False
sns.distplot(titanic['fare'], hist=False, ax=ax2) 

# kde=False
sns.distplot(titanic['fare'], kde=False, ax=ax3)        

# 차트 제목 표시
ax1.set_title('titanic fare - hist/ked')
ax2.set_title('titanic fare - ked')
ax3.set_title('titanic fare - hist')

plt.show()
```

![seaborn_histogram,kde](https://user-images.githubusercontent.com/64063767/97000514-c83f2000-1571-11eb-8e6c-265bf85eac48.png)

---

- **히트맵** `sns.heatmap()`

```python
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('darkgrid')

# 피벗테이블로 범주형 변수를 각각 행, 열로 재구분하여 정리
table = titanic.pivot_table(index=['sex'], columns=['class'], 
                            aggfunc='size') # aggfunc, 데이터 값의 크기를 기준으로 집계
display(table)

# 히트맵 그리기
sns.heatmap(table,                  # 데이터프레임
            annot=True, fmt='d',    # 데이터 값 표시 여부, 정수형 포맷
            cmap='YlGnBu',          # 컬러 맵
            linewidth=.5,           # 구분 선
            cbar=False)             # 컬러 바 표시 여부

plt.show()
```

![seaborn_heatmap](https://user-images.githubusercontent.com/64063767/97000854-54514780-1572-11eb-95d5-5502dab25989.png)

---

- **범주형 데이터의 산점도** `sns.stripplot()` `sns.swarmplot()`

```python
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')

# 그래프 객체 생성 (figure에 2개의 서브 플롯을 생성)
fig = plt.figure(figsize=(20,10))   
ax1 = fig.add_subplot(1,2, 1)
ax2 = fig.add_subplot(1,2, 2)
 
# 이산형 변수의 분포 - 데이터 분산 미고려
sns.stripplot(x="class",      # x축 변수
              y="age",        # y축 변수           
              data=titanic,   # 데이터셋 - 데이터프레임
              ax=ax1)         # ax 객체 - 1번째 그래프 

# 이산형 변수의 분포 - 데이터 분산 고려 (중복 X) 
sns.swarmplot(x="class",      # x축 변수
              y="age",        # y축 변수
              data=titanic,   # 데이터셋 - 데이터프레임
              ax=ax2)         # ax 객체 - 2번째 그래프        

# 차트 제목 표시
ax1.set_title('Strip Plot')
ax2.set_title('Strip Plot')

plt.show()
```

![seaborn_stripplot,swarmplot](https://user-images.githubusercontent.com/64063767/97001235-05f07880-1573-11eb-8c13-ab3bf0ba15fe.png)

---

- **막대 그래프** `sns.barplot()`

```python
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')

# 그래프 객체 생성 (figure에 3개의 서브 플롯을 생성)
fig = plt.figure(figsize=(15,5))   
ax1 = fig.add_subplot(1,3, 1)
ax2 = fig.add_subplot(1,3, 2)
ax3 = fig.add_subplot(1,3, 3)
 
# x축, y축에 변수 할당
sns.barplot(x='sex', y='survived', data=titanic, ax=ax1) 

# x축, y축에 변수 할당하고 hue 옵션 추가 
sns.barplot(x='sex', y='survived', hue='class', data=titanic, ax=ax2) 

# x축, y축에 변수 할당하고 hue 옵션을 추가하여 누적 출력 (dodge=False --> stacked)
sns.barplot(x='sex', y='survived', hue='class', dodge=False, data=titanic, ax=ax3)

# 차트 제목 표시
ax1.set_title('titanic survived - sex')
ax2.set_title('titanic survived - sex/class')
ax3.set_title('titanic survived - sex/class(stacked)')

plt.show()
```

![seaborn_barplot](https://user-images.githubusercontent.com/64063767/97001545-7d260c80-1573-11eb-9742-514f5534addf.png)

---

- **빈도 그래프** `sns.countplot()`

```python
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')

# 그래프 객체 생성 (figure에 3개의 서브 플롯을 생성)
fig = plt.figure(figsize=(15,5))   
ax1 = fig.add_subplot(1,3, 1)
ax2 = fig.add_subplot(1,3, 2)
ax3 = fig.add_subplot(1,3, 3)
 
# 기본값 (개수를 세고 막대그래프로 그려줌)
sns.countplot(x='class', palette='Set1', data=titanic, ax=ax1) 

# hue 옵션에 'who' 추가 
sns.countplot(x='class', hue='who', palette='Set2', data=titanic, ax=ax2) 

# dodge=False 옵션 추가 (축 방향으로 분리하지 않고 누적 그래프 출력)
sns.countplot(x='class', hue='who', palette='Set3', dodge=False, data=titanic, ax=ax3)

# 차트 제목 표시
ax1.set_title('titanic class')
ax2.set_title('titanic class - who')
ax3.set_title('titanic class - who(stacked)')

plt.show()
```

![seaborn_countplot](https://user-images.githubusercontent.com/64063767/97001940-308f0100-1574-11eb-97ca-d79774d41cfe.png)

---

- **박스 플롯/바이올린 그래프** `sns.boxplot()` `sns.violinplot()`

```python
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')

# 그래프 객체 생성 (figure에 4개의 서브 플롯을 생성)
fig = plt.figure(figsize=(20,10))   
ax1 = fig.add_subplot(2,2, 1)
ax2 = fig.add_subplot(2,2, 2)
ax3 = fig.add_subplot(2,2, 3)
ax4 = fig.add_subplot(2,2, 4)
 
# 박스 플롯 - 기본값
sns.boxplot(x='alive', y='age', data=titanic, ax=ax1) 

# 박스 플롯 - hue 변수 추가
sns.boxplot(x='alive', y='age', hue='sex', data=titanic, ax=ax2) 

# 바이올린 그래프 - 기본값
sns.violinplot(x='alive', y='age', data=titanic, ax=ax3) 

# 바이올린 그래프 - hue 변수 추가
sns.violinplot(x='alive', y='age', hue='sex', data=titanic, ax=ax4) 

plt.show()
```

![seaborn_boxplot,violinplotpng](https://user-images.githubusercontent.com/64063767/97002441-f4a86b80-1574-11eb-8dd2-2f1bafb9299b.png)

---

- **조인트 그래프** `sns.jointplot()`

```python
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')

# 조인트 그래프 - 산점도(기본값)
j1 = sns.jointplot(x='fare', y='age', data=titanic) # 조인트 그래프는 ax객체를 인자로 받지 못함

# 조인트 그래프 - 회귀선
j2 = sns.jointplot(x='fare', y='age', kind='reg', data=titanic) 

# 조인트 그래프 - 육각 그래프
j3 = sns.jointplot(x='fare', y='age', kind='hex', data=titanic) 

# 조인트 그래프 - 커널밀도 그래프
j4 = sns.jointplot(x='fare', y='age', kind='kde', data=titanic) 

# 차트 제목 표시
j1.fig.suptitle('titanic fare - scatter', size=15)
j2.fig.suptitle('titanic fare - reg', size=15)
j3.fig.suptitle('titanic fare - hex', size=15)
j4.fig.suptitle('titanic fare - kde', size=15)

plt.show()
```

| ![seaborn_jointplot(scatter)](https://user-images.githubusercontent.com/64063767/97003610-a2684a00-1576-11eb-896e-169aa0e268a4.png) | ![seaborn_jointplot(reg)](https://user-images.githubusercontent.com/64063767/97003625-a98f5800-1576-11eb-9716-a92feb42e7f2.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![seaborn_jointplot(hex)](https://user-images.githubusercontent.com/64063767/97003645-b2802980-1576-11eb-880c-164317a2f127.png) | ![seaborn_jointplot(kde)](https://user-images.githubusercontent.com/64063767/97003668-bb70fb00-1576-11eb-8917-22e13b53ccb8.png) |

---

- **조건을 적용하여 화면을 그리드로 분할하기** `sns.FacetGrid()`

```python
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')

# 조건에 따라 그리드 나누기(빈 영역)
g = sns.FacetGrid(data=titanic, col='who', row='survived') 

# 그래프 적용하기
g = g.map(plt.hist, 'age')
```

![seaborn_FacetGrid](https://user-images.githubusercontent.com/64063767/97004134-8913cd80-1577-11eb-900f-34e7a47d88f4.png)

---



## (2) <span style="color:red;">Folium</span>

> Leaflet 기반 지도시각화 라이브러리

```python
import pandas as pd
import folium

# 대학교 리스트를 데이터프레임 변환
df = pd.read_excel('../data/서울지역 대학교 위치.xlsx')
df.columns = ["학교명", "위도", "경도"]

# 서울 지도 만들기 (초기 위치는 위도의 평균, 경도의 평균으로 지정 권장)
seoul_map = folium.Map(location=[37.55,126.98], zoom_start=12) # folium 지도 객체 생성

# 대학교 위치정보를 Marker로 표시
for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    folium.Marker([lat, lng], popup=name).add_to(seoul_map)
display(seoul_map)

# 지도를 HTML 파일로 저장하기
seoul_map.save('../output/seoul_colleges.html')
```

![folium_1](https://user-images.githubusercontent.com/64063767/97004515-22db7a80-1578-11eb-9225-f3d1b02df415.png)

---



```python
import pandas as pd
import folium
import json

# 경기도 인구변화 데이터를 불러와서 데이터프레임으로 변환
file_path = '../data/경기도인구데이터.xlsx'
df = pd.read_excel(file_path, index_col='구분')  
df.columns = df.columns.map(str)

# 경기도 시군구 경계 정보를 가진 geo-json 파일 불러오기
geo_path = '../data/경기도행정구역경계.json'
try:
    geo_data = json.load(open(geo_path, encoding='utf-8'))
except:
    geo_data = json.load(open(geo_path, encoding='utf-8-sig'))

# 경기도 지도 만들기
g_map = folium.Map(location=[37.5502,126.982], tiles='Stamen Terrain', zoom_start=9)

# 출력할 연도 선택 (2007 ~ 2017년 중에서 선택)
year = '2017'

# Choropleth 클래스로 단계구분도 표시하기
choropleth = folium.Choropleth(geo_data=geo_data,  # 지도 경계
                               data = df[year],    # 표시하려는 데이터
                               columns = [df.index, df[year]],  # 열 지정
                               fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.3,
                               threshold_scale=[10000, 100000, 300000, 500000, 700000],
                               key_on='feature.properties.name').add_to(g_map)

choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(['name'], labels=False))

display(g_map)

# 지도를 HTML 파일로 저장하기
g_map.save('../output/gyonggi_population_' + year + '_2.html')
```

![folium_2](https://user-images.githubusercontent.com/64063767/97005595-9fbb2400-1579-11eb-8155-0cb06436aa48.png)