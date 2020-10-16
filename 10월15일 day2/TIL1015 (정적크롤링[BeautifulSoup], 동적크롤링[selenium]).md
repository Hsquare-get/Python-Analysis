# TIL1015 (정적크롤링[BeautifulSoup], 동적크롤링[selenium])

## 1. 정적크롤링 (<span style = "color:red;">BeautifulSoup</span>)

> HTML 및 XML 파일에서 데이터를 추출하기 위한 파이썬 라이브러리
>
> HTML 및 XML 파일의 내용을 읽을 때 다음의 Parser 이용. html.parser / lxml / lxml-xml / html5lib

```python
from bs4 import BeautifulSoup

# HTML 문서를 파싱하고 bs4.BeautifulSoup 객체 생성
bs = BeautifulSoup(html_doc, 'html.parser')

# 태그 접근
bs.h1.name
bs.h1['속성명']
bs.h1.attrs # 모든 속성 추출

# 컨텐츠 추출
bs.h1.string # bs.h1.string.strip()
bs.h1.text # bs.h1.text.strip()
bs.h1.contents
bs.h1.strings
```



- 태그 찾기 주요 메서드

  - **find()** : 제일 먼저 인식되는 태그 하나를 찾음 (bs.element.Tag 객체로 리턴, 없으면 None 리턴)

    ```python
    bs.find('div') == bs.find_all('div', limit=1)
    ```

  - **find_all()** : 모든 태그들을 찾음 (bs4.element.ResultSet 객체로 리턴)

    ```python
    bs.find_all('div')
    bs.find_all(['p', 'img'])
    bs.find_all(re.compile('^b'))
    bs.find_all(id='link2')
    bs.find_all(id=re.compile('para$'))
    bs.find_all('a', class_='sister') # class는 예약어이기 때문에 class_ 사용
    bs.find_all(src=re.compile('png$'), id='link1')
    bs.find_all(text='example') # 정확하게 example만
    bs.find_all(text=re.compile('example')) # example을 포함하여
    bs.find_all(text=re.compile('^test'))
    bs.find_all('a', text='python')
    bs.find_all('a', limit=2) # 2개까지만 찾음
    ```

  - **select()** : css 선택자에 알맞는 돔객체를 찾는 메서드 <span style="color:red;">**(리스트 객체로 반환)**</span>

    ```python
    bs.select('div')
    bs.select('.class')
    bs.select('#id')
    
    bs.select('상위태그명 > 자식태그명 > 자손태그명')
    bs.select('상위태그명.class명 > 자식태그명.class명')
    bs.select('상위태그명.class명 자손태그명')
    bs.select('#id명 > 자식태그명.class명')
    bs.select('태그명[속성]')
    bs.select('태그명[속성=값]')
    bs.select('태그명[속성$=값]')
    bs.select('태그명[속성^=값]')
    bs.select('태그명:nth-of-type(3)')
    ```




## (2) 동적크롤링 (<span style = "color:red;">selenium</span>)

| 정적 웹페이지                                                | 동적 웹페이지                                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 웹 서버에서 전송된 웹 페이지 소스(*개발자 도구X*)에서 화면에 렌터링된 내용을 모두 찾을 수 있는 경우 | 웹 서버에서 전송된 웹 페이지의 소스에서 화면에 렌더링된 내용을 일부 찾을 수 없는 경우 |
| HTML만으로 작성되거나 **HTML**, **CSS**로만 구현된 경우      | HTML, CSS 외에 **JavaScript** 프로그래밍 언어로 브라우저에서 실행시킨 코드에 의해 웹 페이지의 내용이 렌더링시 자동으로 생성되는 페이지 |

> **selenium** : 다양한 플랫폼과 언어를 지원하는 웹 브라우저를 자동화하는 도구 모음

- WebDriver API를 통해 운영체제에 설치된 크롬이나 파이어폭스 등의 브라우저를 기동시키고 웹 페이지를 로드하고 제어
- 브라우저를 직접 동작시킨다는 것은 JavaScript에 의해 생성되는 컨텐츠와 Ajax 통신 등을 통해 뒤늦게 불려오는 컨텐츠를 처리할 수 있다는 것을 의미 

> **WebDriver API** : 간결한 프로그래밍 인터페이스를 제공하도록 설계, 동적 웹 페이지를 보다 잘 지원할 수 있도록 개발

- WebDriver의 목표 : 최신 고급 웹 응용 프로그램 테스트 문제에 대한 향상된 지원을 제공하는 잘 디자인된 객체 지향 API를 제공하는 것
- Selenium-WebDriver는 자동화를 위한 각 브라우저의 기본 지원을 사용하여 브라우저를 직접 호출

```python
# WebDriver 객체 생성 (세션 정보도 포함)
driver = webdriver.Chrome("C:/PyStexam/selenium/chromedriver")
driver.implicitly_wait(3) # 렌더링 끝날때까지 3초 기다리기
# 렌더링이 일찍되면 더 기다리지 않고 다음 코드 수행, 한번만 설정하면 driver를 사용하는 모든 코드에 적용

# 페이지 가져오기
diver.get('url')
```

| 조건에 맞는 요소 한 개 찾기                                | 조건에 맞는 모든 요소 찾기                                   |
| ---------------------------------------------------------- | ------------------------------------------------------------ |
| driver.find_element_by_xxx('')                             | driver.find_element<span style = "color:blue;">**s**</span>_by_xxx('') |
| <span style = "color:red;">**WebElement 객체 리턴**</span> | <span style = "color:red;">**list 객체 리턴**</span>         |

- 태그의 id 속성값으로 element 찾기

  ```python
  element = driver.find_element_by_id('id')
  ```

- 태그의 class 속성 값으로 element 찾기

  ```python
  element = driver.find_element_by_class_name('class')
  ```

- 태그명으로 element 찾기

  ```python
  element = driver.find_element_by_tag_name('h1')
  ```

- 링크 텍스트로 element 찾기

  ```python
  # <a href="https://www.python.org/">파이썬 학습 사이트</a>
  element = driver.find_element_by_link_text('파이썬 학습 사이트')
  ```

- 부분 링크 텍스트로 element 찾기

  ```python
  # <a href="https://www.python.org/">파이썬 학습 사이트</a>
  element = driver.find_elements_by_partial_link_text('사이트')
  ```

- CSS 선택자로 element 찾기

  ```python
  element = driver.find_element_by_css_selector('section>h2')
  ```

- XPath로 element 찾기

  ```python
  element = driver.find_element_by_xpath('//*[@id="f_subtitle"]')
  ```

---

- 요소의 정보 추출

```python
element = driver.find_element_by_id('element_id')
element.tag_name # 태그명
element.text # 텍스트 형식의 컨텐츠
element.get_attribute('속성명') # 속성값 
```

