# <span style="color:blue;">Apache Hadoop</span>

> Hadoop 시스템을 이용하는 기기의 사양을 타지 않는다. (노트북, 라즈베리파이, 일반PC..)

#### <span style="color:red;">HDFS</span> : 데이터 분산 저장 시스템(Storage)

#### <span style="color:red;">MapReduce</span> : 데이터 분산 처리 시스템(Computation)



#### 클러스터

- 여러대의 컴퓨터들이 연결되어 하나의 시스템처럼 동작하는 컴퓨터들의 집합



#### Hadoop HDFS 명령어

| 명령어                                                       | 의미                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| hdfs dfs -ls /[디렉토리명 또는 파일명]                       | 지정된 디렉토리의 파일리스트 또는 지정된 파일의 정보를 보여준다 |
| hdfs dfs -ls -R /[디렉토리명]                                | 지정된 디렉토리의 파일리스트 및 서브디렉토리들의 파일 리스트도 보여준다 |
| hdfs dfs -mkdir /디렉토리명                                  | 지정된 디렉토리를 생성한다                                   |
| hdfs dfs -cat /[디렉토리/]파일                               | 지정된 파일의 내용을 화면에 출력한다                         |
| hdfs dfs -put 사용자계정로컬파일 HDFS디렉토리[/파일]         | 지저왼 사용자계정 로컬 파일시스템의 파일을 HDFS 상 디렉토리의 파일로 복사한다 |
| hdfs dfs -get HDFS디렉토리의파일 사용자계정로컬디렉토리[/파일] | 지정된 HDFS상의 파일을 사용자계정 로컬 파일시스템의 디렉토리나 파일로 복사한다 |
| hdfs dfs -rm /[디렉토리]/파일                                | 지정된 파일을 삭제한다                                       |
| hdfs dfs -rm -r /디렉토리                                    | 지정된 디렉토리를 삭제, 비어있지 않은 디렉토리도 삭제하며 서브 디렉토리까지도 삭제한다 |
| hdfs dfs -tail /[디렉토리]/파일                              | 지정된 파일의 마지막 1kb 내용을 화면에 출력한다              |
| hdfs dfs -chmod 사용자허가모드 /[디렉토리명 또는 파일명]     | 지정된 디렉토리 또는 파일의 사용자 허가 모드를 변경한다      |
| hdfs dfs -mv /[디렉토리]/old파일/[디렉토리]/new파일          | 지정된 디렉토리의 파일을 다른 이름으로 변경하거나 다른 폴더로 이동한다 |



#### <span style="color:red;">Hadoop MapReduce</span>

> 구글에서 대용량 데이터 처리를 분산 병렬 컴퓨팅에서 처리하기 위한 목적으로 제작한 소프트웨어 프레임워크다. 대용량 데이터를 신뢰도가 낮은 컴퓨터로 구성된 클러스터 환경에서 병렬 처리를 지원하기 위해서 개발됐다.

![mapreduce](https://user-images.githubusercontent.com/64063767/98115573-63c57e80-1eea-11eb-8a54-034283231a77.png)

> MapReduce는 Hadoop 클러스터의 데이터를 처리하기 위한 시스템으로 총 2개(Map, Reduce)의 단계로 구성된다. Map과 Reduce 사이에는 shuffle과 sort라는 단계가 존재한다. 각 Map task는 전체 데이터 셋에 대해서 별개의 부분에 대한 작업을 수행하게 되는데, 기본적으로 하나의 HDFS block을 대상으로 수행하게 된다. 모든 Map task가 종료되면, MapReduce 시스템은 중간 데이터를 Reduce 단계를 수행할 노드로 분산하여 전송한다.
>
> Distributed File System에서 수행되는 MapReduce 작업이 끝나면 HDFS에 파일이 써지고, MapReduce 작업이 시작할 때는 HDFS로부터 파일을 가져오는 작업이 수행된다.

![mapreduce process](https://user-images.githubusercontent.com/64063767/98115946-ef3f0f80-1eea-11eb-846c-ac2e0e7ee542.png)

> MapReduce는 데이터를 개별로 가공 및 필터링하거나, 어떤 키 값에 기반해 데이터를 분류하거나, 분류한 데이터로 통계치를 계산하는 등, 수많은 데이터 처리에서 사용되고 있는 기법들을 일반화 하고있다. map() 함수와 reduce() 함수는 한 번에 처리할 수 있는 데이터와 데이터 전달 방법 등이 다르다.
>
> map() 함수는 처리 대상 데이터 전체를 하나씩, 하나씩 처리한다. 처리대상 데이터간에 의존관계가 없고 독립적으로 실행 가능하며 처리나 순서를 고려하지 않아도 되는 처리에 적합하다(전처리)
>
> reduce() 함수에는 키와 연관된 복수의 데이터가 전달된다. 또한 reduce() 함수에 전달되는 데이터는 키 값으로 정렬되어 있다. 그룹화된 복수의 데이터를 필요로 하는 처리 또는 순서를 고려해야 하는 처리에 적합하다(그룹별합계)



![mapreduce(apache hadoop vs apache spark)](https://user-images.githubusercontent.com/64063767/98116452-9fad1380-1eeb-11eb-8369-fb106cb25351.png)



# <span style="color:blue;">Apache SPARK</span>

> Spark는 빅데이터 기술발전과 함께 빅데이터용 데이터 처리 플랫폼이자 프로그래밍 인터페이스이다.
>
> 스칼라 또는 자바로 프로그래밍 설계되어있다. 파이썬으로 이용도 가능하다.
>
> 광범위한 데이터 처리 및 분석 작업의 성능과 효율성을 극대화할 수 있다.
>
> **Hadoop의 MapReduce의 수행속도를 비약적으로 개선시켜서 나온 것이 Spark이다**



Q. SPARK가 왜 좋은가? 얼마나 좋은가? SPARK가 왜 나왔는지 아는가?



## (1) Apache Spark

> Apache Spark는 메모리 내 처리를 지원하여 빅데이터를 분석하는 애플리케이션의 성능을 향상시키는 오픈소스 병렬처리 프레임워크이다. 빅데이터 솔루션은 기존 데이터베이스에 비해 너무 크거나 복잡한 데이터를 처리하도록 설계됐다.
>
> Spark는 대량의 데이터를 고속 병렬 분산처리한다. 데이터소스로부터 데이터를 읽어들인 뒤 스토리지 I/O와 네트워크 I/O를 최소화하도록 처리한다. 따라서 Spark는 동일한 데이터에 대한 변환처리가 연속으로 이루어지는 경우와 머신러닝처럼 결과셋을 여러 번 반복해 처리하는 경우에 적합하다.



#### [Spark의 데이터 처리 단위 : RDD]

> 데이터셋을 추상적으로 다루기 위한 RDD(Resilient Distributed Dataset, 내결함성 분산 데이터셋)라는 데이터셋이 있으며, RDD가 제공하는 API로 변환과 액션 기능을 구현한다.

- RDD(Resilient Distributed Dataset)

  - Spark에서 처리되는 데이터는 RDD 객체로 생성하여 처리한다.

  - RDD 객체는 두가지 방법으로 생성가능

    - Collection 객체를 만들어서
    - HDFS의 파일을 읽어서

    

- RDD 객체의 특징 : 

  - **Read Only**(immutable)
  - 1~n 개의 partition으로 구성 가능
  - 병렬적(분산) 처리가 가능하다.
  - RDD의 연산은 <span style="color:red;">**Transformation**</span> 연산과 <span style="color:red;">**Action**</span> 연산으로 나뉜다.
  - Transformation은 <span style="color:red;">**Lazy-execution**</span>을 지원한다. 
    - Lineage만 작성해놨다가 action api가 호출이 되면 그제서야 모든 작업을 최적화된 경로로 처리한다
    - **Lineage** : 작업순서를 기록해 DAG로 표현한 것
  - Lineage를 통해서 fault tolerant(결함 내성)를 확보한다.

![RDD](https://user-images.githubusercontent.com/64063767/98117433-17c80900-1eed-11eb-8479-bc1cfae32d8d.png)



#### [Transformation & Action]

![transformations actions](https://user-images.githubusercontent.com/64063767/98117612-5fe72b80-1eed-11eb-8cb1-d0f5dca389bb.png)

- <span style="color:red;">**Transformation**</span>

  - 연산의 수행결과가 **RDD**이면 **Transformation**
  - 기존 RDD에서 데이터를 조작하여 새로운 RDD를 생성하는 함수(연산)
  - Lineage를 만들어가는 과정

  

- <span style="color:red;">**Action**</span>
  - 연산의 수행 결과가 **정수, 리스트, 맵** 등 RDD가 아닌 다른 타입이면 **Action** 
  - RDD에서 RDD가 아닌 타입의 data로 변환하는 함수(연산)
  - Lineage를 실행하고 결과를 만듬



##### <span style="color:red;">Lazy-execution</span>

![Lineage](https://user-images.githubusercontent.com/64063767/98118571-c456ba80-1eee-11eb-9203-47e469ed8042.png)

> Action 연산이 실행되기 전에는 Transformation 연산이 처리되지 않는 것을 의미한다. Transformation 연산은 관련 메서드를 호출하여 연산을 요청해도 실제 수행은 되지 않고 연산 정보만 보관한다. 이렇게 Transformation 연산 정보를 보관한 것을 Lineage(리니지)라고 한다. 보관만 하다가 첫 번째 Action 연산이 수행될 때 모든 Lineage에 보관된 Transformation 연산을 한번에 처리한다.
>
> Lazy-execution과 Lineage를 활용함으로써 처리 효율을 높이고 클러스터 중 일부 고장으로 작업이 실패해도 Lineage를 통해 데이터를 복구한다.



#### [RDD & DataFrame & DataSet]

- RDD(2011) --> DataFrame(2013) --> DataSet(2015)

- **Apache Spark**는 <span style="color:red;">**특정한 데이터셋에 대하여 반복처리와 연속적으로 이루어지는 변환처리를 고속화**</span>할 목적으로 개발됐다.

  - 반복처리 + 연속으로 이루어지는 변환처리의 고속화
  - 시행착오에 적합한 환경제공
  - 서로 다른 처리를 통합해 이용할 수 있는 환경

  

## (2) PySpark

- Spark 자체는 3.8로 기동시키고 Python은 3.7 버전이기 때문에 버전간 호환이 안되는 에러가 발생할 수 있다

- 환경변수를 셋팅해주면 오류 해결 가능

- 시스템 변수 등록
  - 변수 이름 : PYSPARK_PYTHON 
  - 변수 값 : C:\Users\user\anaconda3\envs\pydatavenv\python



> PySpark는 Apache Spark 기능을 사용하여 Python 애플리케이션을 실행하기 위해 Python으로 작성된 Spark 라이브러리이다. PySpark를 사용하면 분산 클러스터(다중노드)에서 애플리케이션을 병렬로 실행할 수 있다.
>
> Spark는 Scala라는 언어로 작성되었으며 Spark 프로그래밍에는 Scala가 가장 많이 사용되고 있다. 또한 데이터 처리나 분석 프로그래밍에 많이 사용되는 Python으로도 개발할 수 있게 Py4J를 사용하여 Python 용으로 출시된 API가 바로 PySpark이다. Py4JSpark 내에 통합된 Java 라이브러리이며 Python이 JVM 개체와 동적으로 인터페이싱할 수 있도록 하므로 PySpark를 실행하려면 Python 뿐만 아니라 Java 개발 환경(JDK)도 설치되어 있어야한다.
>
> 또한 개발을 위해 Spyder IDE, Jupyter 노트북(랩)과 같은 많은 유용한 도구와 함께 제공되는 Anaconda 배포(머신러닝 커뮤니티에서 널리 사용됨)를 사용하여 PySpark 애플리케이션을 실행할 수 있다.
>
> PySpark는 대규모 데이터 셋을 효율적으로 처리하기 때문에 NumPy, Pandas, TensorFlow를 포함하여 Python으로 작성된 데이터 과학 라이브러리와 함께 많이 사용된다.



- PySpark 장점
  - PySpark는 분산 방식으로 데이터를 효율적으로 처리할 수 있는 범용 In-Memory 분산처리 엔진이다.
  - PySpark에서 실행되는 애플리케이션은 기존 시스템보다 100배 빠르다.
  - 데이터 수집 파이프 라인에 PySpark를 사용하면 큰 이점을 얻을 수 있다.
  - PySpark를 사용하여 Hadoop HDFS, AWS S3 및 여러 파일 시스템의 데이터를 처리할 수 있다.
  - PySpark는 Streaming 및 Kafka를 사용하여 실시간 데이터를 처리하는데도 사용된다.
  - PySpark Streaming을 사용하면 파일 시스템에서 파일을 스트리밍하고 소켓에서 스트리밍 할 수도 있다.
  - PySpark에는 기본적으로 기계학습(머신러닝) 및 그래프 라이브러리가 있다.



- PySpark 아키텍처

> Apache Spark는 마스터를 '드라이버'라 하고 슬레이브를 '작업자'라고 하는 **마스터-슬레이브 아키텍처**에서 작동한다. Spark 애플리케이션을 실행하면 Spark Driver가 애플리케이션의 진입점인 컨텍스트를 생성하고 모든 작업(변환 및 작업)이 작업자 노드에서 실행되고 리소스는 Cluster Manager에서 관리된다.



- PySpark 모듈 및 패키지
  - PySpark RDD (pyspark.RDD)
  - PySpark DataFrame 및 SQL (pyspark.sql)
  - PySpark 스트리밍 (pyspark.streaming)
  - PySpark Mlib (pyspark.ml, pyspark.mllib)
  - PySpark GraphFrames (GraphFrames)
  - PySpark 리소스 (pyspark.resource)

