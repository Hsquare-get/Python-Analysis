# TIL1014 (웹페이지 요청, BeautifulSoup)

## 1-1. urllib 기본 패키지를 활용한 웹페이지 요청

> 파이썬의 표준 라이브러리

| 모듈               | 기능                                                         |
| ------------------ | ------------------------------------------------------------ |
| urllib.request     | URL 문자열을 가지고 <span style="color:red;">**요청**</span> 기능 제공 |
| urllib.response    | urllib 모듈에 의해 사용되는 <span style="color:red;">**응답**</span> 기능관련 클래스들 제공 |
| urllib.parse       | URL 문자열을 파싱하여 <span style="color:red;">**해석**</span>하는 기능 제공 |
| urllib.error       | urllib.request에 의해 발생하는 예외 클래스들 제공            |
| urllib.robotparser | robots.txt 파일을 구문 분석하는기능 제공                     |

### (I) urllib.request 모듈

- URL 문자열을 가지고 HTTP 요청을수행

- urlopen() 함수를 사용하여 웹 서버에 페이지를 **요청**하고, 서버로부터 받은 **응답**을 저장하여 <span style="color:red;">**응답객체(http.client.HTTPResponse)로 반환**</span>

  ```python
  res = urllib.request.urlopen("url")
  ```

- http.client.HTTPResponse 클래스

  - res.read() : 웹 서버가 전달한 데이터(응답 body)를 <span style="color:red;">**바이트열(Bytes 객체)**</span>로 읽어 옴 (바이트열은 16진수로 이루어진 수열)

    ```python
    res.read.decode('utf-8')
    ```

  - res.info() : 웹 페이지의 문자 셋 정보를 페이지 소스보기말고도 파이썬으로도 확인할 수 있음

    ```python
    res.info().get_content_charset()
    ```



### (II) urllib.parse 모듈

> 웹 서버에 페이지 or 정보를 요청할 때 함께 전달하는 데이터

- GET 방식 요청 : Query 문자열 ####################

- POST 방식 요청 : 요청 파라미터 ###################

- urllib.parse.urlparse('url') : 아규먼트로 지정된 URL 문자열의 구성정보를 저장하는 **urllib.parse.ParseResult 객체**를 리턴함 

  ```python
  urlparse('https://movie.daum.net/moviedb/main?movieId=93252')
  >>> ParseResult(scheme='https', netloc='movie.daum.net', path='/moviedb/main', params='', query='movieId=93252', fragment='')
  ```

- urllib.parse.urlencode() : 메서드의 아규먼트로 지정된 name : value로 구성된 딕셔너리 정보를 **정해진 규격의 Query 문자열 또는 요청 파라미터 문자열로 리턴**함

  ```python
  urlencode({'number': 12524, 'type': 'issue', 'action': 'show'})
  >>> number=12524&type=issue&action=show
  urlencode({'addr': '서울시 강남구'})
  >>> addr=%EC%84%9C%EC%9A%B8%EC%8B%9C+%EA%B0%95%EB%82%A8%EA%B5%AC
  ```

- <span style="color:blue;">**GET 방식 요청**</span> : <span style="color:red;">**Query 문자열을 포함하여 요청**</span>

  ```python
  params = urllib.parse.urlencode({'name': '최현호', 'age': 27})
  url = "http://unico2013.dothome.co.kr/crawling/get.php?%s" % params
  urllib.request.urlopen(url)
  ```

- <span style="color:blue;">**POST 방식 요청**</span> : <span style="color:red;">**요청 body 안에 요청 파라미터를 포함하여 요청하는 것**</span>

  > GET 방식과 같이 name : value로 구성되는 문자열을 만듦
  >
  > POST 방식 요청에서는 **바이트열 형식**으로 전달해야 하므로, **encode('ascii')** 메서드를 호출하여 바이트열로 변경

  ```python
  # 방법 1
  data = urllib.parse.urlencode({'name': '유니코', 'age': 10})
  data = data.encode('ascii') # b'name=%EC%9C%A0+%EB%8B%88%EC%BD%94&age=10'
  
  url = 'http://unico2013.dothome.co.kr/crawling/post.php'
  urllib.request.urlopen(url, data)
  
  # 방법 2 : URL 문자열과 요청 파라미터 문자열을 지정한 urllib.request.Request 객체 생성
  data = urllib.parse.urlencode({'name': '유니코', 'age': 10})
  postdata = data.encode('ascii')
  
  req = urllib.request.Request(url='http://unico2013.dothome.co.kr/crawling/post.php', data = postdata)
  urllib.request.urlopen(req)
  ```



## 1-2. requests 패키지를 활용한 웹페이지 요청

| urllib 패키지                                    | requests 패키지                                              |
| ------------------------------------------------ | ------------------------------------------------------------ |
| 인코딩하여 바이너리 형태로 데이터 전송           | 딕셔너리 형태로 데이터 전송                                  |
| 요청 방식(GET, POST)에 따라서 구현 방법이 달라짐 | request() 함수 호출시 요청 메서드(GET, POST)를 명시하여 요청 |

### (I) requests.request() 함수

- requests.request(method, url, **kwargs)

```python
reqeusts.request('GET', url, params=None) # GET 방식 요청
requests.get(url, params=None) # GET 방식 요청

reqeusts.request('POST', url, data=None, json=None) # POST 방식 요청
requests.post(url, data=None, json=None) # POST 방식 요청
```



- requests.models.Response 객체로 리턴됨

  - Text

    - <span style="color:red;">**문자열 형식(str 객체)으로**</span> 응답 컨텐츠 추출

    - 추출할 때 문자셋이 'euc-kr'일 경우 한글이 깨짐

      ```python
      r.encoding='utf-8'
      ```

  - Content

    - <span style="color:red;">**바이트열 형식(Bytes 객체)으로**</span> 응답 컨텐츠 추출

    - **응답 컨텐츠가 이미지**와 같은 바이너리 형식인 경우 사용

    - 한글이 들어간 문자열 형식인 경우

      ```python
      r.content.decode('utf-8')
      ```



## 2. BeautifulSoup

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
bs.h1.string # bs.h1.string_strip()
bs.h1.text # bs.h1.text_strip()
bs.h1.contents
bs.h1.strings
```



- 태그 찾기 주요 메서드

  - **find()** : 제일 먼저 인식되는 태그 하나를 찾음 (bs.element.Tag 객체로 리턴, 없으면 None 리턴)

    ```python
    find('div') == find_all('div', limit=1)
    ```

  - **find_all()** : 모든 태그들을 찾음 (bs4.element.ResultSet 객체로 리턴)

    ```python
    find_all('div')
    find_all(['p', 'img'])
    find_all(re.compile('^b'))
    find_all(id='link2')
    find_all(id=re.compile('para$'))
    find_all('a', class_='sister') # class는 예약어이기 때문에 class_ 사용
    find_all(src=re.compile('png$'), id='link1')
    find_all(text='example') # 정확하게 example만
    find_all(text=re.compile('example')) # example을 포함하여
    find_all(text=re.compile('^test'))
    find_all('a', text='python')
    find_all('a', limit=2) # 2개까지만 찾음
    ```

  - **select()** : css 선택자에 알맞는 돔객체를 찾는 메서드

    ```python
    select('div')
    select('.class')
    select('#id')
    
    select('상위태그명 > 자식태그명 > 자손태그명')
    select('상위태그명.class명 > 자식태그명.class명')
    select('상위태그명.class명 자손태그명')
    select('#id명 > 자식태그명.class명')
    select('태그명[속성]')
    select('태그명[속성=값]')
    select('태그명[속성$=값]')
    select('태그명[속성^=값]')
    select('태그명:nth-of-type(3)')
    ```

    