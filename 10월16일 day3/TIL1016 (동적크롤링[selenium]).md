# TIL1016 (동적크롤링[selenium])


## (1) 동적크롤링 (<span style = "color:red;">selenium</span>)

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



- Key-In

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/PyStexam/selenium/chromedriver')
driver.implicitly_wait(3)
driver.get('https://www.naver.com/')

element = driver.find_element_by_id('query')
element.send_keys('파이썬')
element.send_keys(Keys.ENTER)

# driver.quit()
```



---



```python
from selenium import webdriver
import time

# 브라우저를 띄우지않고 캡쳐하기 (브라우저에 따라 옵션 제공X)
options = webdriver.ChromeOptions()
options.add_argument('headless') # 브라우저 기동 X
options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome('C:/PyStexam/selenium/chromedriver', options=options)
driver.get('http://www.python.org/')
driver.implicitly_wait(3)

driver.get_screenshot_as_file('C:/PyStexam/10월16일 day3/main_main_headless.png')

print('캡쳐 저장 완료')
time.sleep(2)
driver.quit()
```



```python
# 스타벅스 매장정보 크롤링 (스크롤 다운)
from selenium import webdriver
import time

driver = webdriver.Chrome('C:/PyStexam/selenium/chromedriver')
driver.implicitly_wait(3) 
driver.get("https://www.istarbucks.co.kr/store/store_map.do")
time.sleep(2)

loca = driver.find_element_by_class_name('loca_search')
loca.click()
time.sleep(2)

f_link = driver.find_element_by_css_selector("div.loca_step1_cont > ul > li:nth-child(1) > a")
f_link.click()
time.sleep(2)

s_link = driver.find_element_by_css_selector("#mCSB_2_container > ul > li:nth-child(1) > a")
s_link.click()
time.sleep(2)

shopList = driver.find_elements_by_css_selector("#mCSB_3_container > ul > li")

temp_list = []
time.sleep(3)
count = 0
total = len(shopList) # 전체 매장수를 셀 수 있음
print(total)
for shop in shopList:    
    count += 1
    shoplat = shop.get_attribute("data-lat")
    shoplong = shop.get_attribute("data-long")
    shopname = shop.find_element_by_tag_name("strong")
    shopinfo = shop.find_element_by_tag_name("p")
    splitinfo = shopinfo.text.split('\n')
    if(len(splitinfo) == 2):
        addr = splitinfo[0]
        phonenum = splitinfo[1]
    temp_list.append([shopname.text, shoplat, shoplong, addr, phonenum])
    if count != total and count % 3 == 0:
        driver.execute_script("var su = arguments[0]; var dom=document.querySelectorAll('#mCSB_3_container > ul > li')[su]; dom.scrollIntoView();", count)
        
with open('C:/PyStexam/10월16일 day3/starbucks_shop.txt', "wt", encoding="utf-8") as f:
    for item in temp_list:
        f.write(str(item) + '\n')
```



- **iframe** : iframe 요소를 이용하면 해당 html 웹 페이지 안에 어떠한 제한 없이 또 다른 하나의 html 웹 페이지를 삽입할 수 있다. 웹드라이버 객체를 생성해도 원래 웹페이지의 돔객체는 찾을 수 있지만 삽입된 프레임의 돔 객체는 찾을 수 없다.

```python
# 소스코드에서 iframe 찾기 (이외에도 다른방법 존재, ref 참고)
from selenium import webdriver

iframes = driver.find_elements_by_css_selector('iframe')
for iframe in iframes:
    print(iframe.get_attribute('name'))
    
# frame 전환하기 (switch_to.frame)
driver.switch_to.default_content() # 상위 프레임으로 전환
driver.switch_to.frame('프레임이름') # 특정 프레임으로 전환
```

`ref` (https://m.blog.naver.com/PostView.nhn?blogId=kiddwannabe&logNo=221253004219&proxyReferer=https:%2F%2Fwww.google.co.kr%2F)



```python
# 네이버지도에서 검색어정보 크롤링 (스크롤다운 + iframe)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

driver = webdriver.Chrome('C:/PyStexam/selenium/chromedriver')
driver.implicitly_wait(3) 
driver.get('https://map.naver.com/')
time.sleep(2)

target=driver.find_element_by_css_selector(".input_search")
target.send_keys('서울시어린이도서관')
target.send_keys(Keys.ENTER)
time.sleep(2)

driver.switch_to.frame("searchIframe")
while True:
    count = 9
    while True:
        # scroll down 처리
        print("스크롤 : " + str(count))
        try :
            driver.execute_script("var su = arguments[0]; var dom=document.querySelectorAll('#_pcmap_list_scroll_container>ul>li')[su]; dom.scrollIntoView();", count)
            time.sleep(2)
        except :        
            break
        count += 10
    
    names = driver.find_elements_by_css_selector("span.es3Ot")
    addrs = driver.find_elements_by_css_selector("span.gDzVe")
    if len(names) == 0:
        print("추출되는 도서관이 더 이상 없음")
        break
    for i in range(len(names)):
        print(names[i].text, addrs[i].text, sep=", ", end="\n")
    print("------------------------------------------------")
    
    linkurl = '#app-root > div > div > div._2gyDX > a:nth-child(7)'
    try :
        linkNum = driver.find_element_by_css_selector(linkurl)
    except :
        print("더 이상 다음 페이지 없음")
        break
    linkNum.click()  
    time.sleep(5)
    
print("스크래핑 종료")
```

