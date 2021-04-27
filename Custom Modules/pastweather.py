import urllib.request
from bs4 import BeautifulSoup # HTML, XML Document 데이터를 읽기 위한 라이브러리
import pandas as pd
import numpy as np
import datetime as dt
from pytz import timezone
import math
import time


class PastWeather:
    ##### 클래스 변수 선언 #####
    # time info
    now = dt.datetime.now(timezone('Asia/Seoul'))  # 2021-03-14 10:56:23.806631+09:00(KST)
    oneday = dt.timedelta(days=1)

    # parameters
    url = 'http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList'
    serviceKey = '0Nxjl3xb59fkPcq7n0%2FoeaP1%2BvZy8L1l%2B4NunrGvuPrFcORrGfI2caBJ2dzsJA6VZWYw6XGIJ0hH2%2Bx9V74bUQ%3D%3D'
    pageNo = '1'
    numOfRows = '999'  # 가져올 수 있는 1페이지당 최대 결과수
    dataCd = 'ASOS'
    dateCd = 'HR'  # 1시간 단위


    # representation
    def __repr__(self):
        msg = """
            PastWeather 클래스는 기상청으로부터 관측된 어제까지의 과거 날씨를 OpenAPI로 호출하는 클래스입니다.
            매개변수로는 시작날짜와, 지역코드가 있으며 start_day='20210415', stnIds='108' 형식으로 인자를 지정할 수 있습니다.
            """
        return msg


    ##### 초기화 메서드 #####
    def __init__(self, start_day, stnIds):
        self.start_day = start_day
        self.stnIds = stnIds # 108(서울)


    def get_loopCount(self):
        end_day = (PastWeather.now - PastWeather.oneday).strftime('%Y%m%d')  # 20210313 (str)

        url_xml = str(
            PastWeather.url +
            '?serviceKey=' + PastWeather.serviceKey +
            '&dataCd=' + PastWeather.dataCd +
            '&dateCd=' + PastWeather.dateCd +
            '&stnIds=' + self.stnIds +
            '&startDt=' + self.start_day + '&startHh=00' +
            '&endDt=' + end_day + '&endHh=23'
            )

        response = urllib.request.urlopen(url_xml)
        response_code = response.getcode()

        if response_code == 200:
            response_body = response.read().decode('utf-8')  # decode('utf-8') : 바이트열 -> 문자열(복호화)
            soup = BeautifulSoup(response_body, 'html.parser')  # xml도 가능

            totalcount = int(soup.find('totalcount').text)
            # print('totalcount:', totalcount)
            loopCount = math.ceil(totalcount / 999)
            # print('loopCount:', loopCount)

        return loopCount


    def get_start_end_date(self):
        yesterday = (PastWeather.now - PastWeather.oneday).strftime('%Y-%m-%d')  # 2021-03-13 (str)
        timestamp = pd.date_range(start=self.start_day + ' 00', end=yesterday + ' 23', freq='H')
        loopCount = PastWeather.get_loopCount(self)  # get_loopCount() 메서드 호출
        
        start_end_date_arr = []
        if loopCount == 1:
            start_date = str(timestamp[0])
            start_ymd = start_date[:4] + start_date[5:7] + start_date[8:10]
            start_hour = start_date[11:13]

            end_date = str(timestamp[-1])
            end_ymd = end_date[:4] + end_date[5:7] + end_date[8:10]
            end_hour = end_date[11:13]

            start_end_date_arr.append([str(loopCount), start_ymd, start_hour, end_ymd, end_hour])

        else:
            start_dates = timestamp[0::999]
            end_dates = timestamp[998::999]

            for idx, (start_date, end_date) in enumerate(zip(start_dates, end_dates)):
                # Year
                start_year = str(start_date.year)
                end_year = str(end_date.year)

                # Month
                start_month = '0' + str(start_date.month) if len(str(start_date.month)) < 2 else str(start_date.month)
                end_month = '0' + str(end_date.month) if len(str(end_date.month)) < 2 else str(end_date.month)

                # Day
                start_day = '0' + str(start_date.day) if len(str(start_date.day)) < 2 else str(start_date.day)
                end_day = '0' + str(end_date.day) if len(str(end_date.day)) < 2 else str(end_date.day)

                # Hour
                start_hour = '0' + str(start_date.hour) if len(str(start_date.hour)) < 2 else str(start_date.hour)
                end_hour = '0' + str(end_date.hour) if len(str(end_date.hour)) < 2 else str(end_date.hour)

                # start_end_date_arr([호출번호, 시작날짜, 시작시간, 마지막날짜, 마지막시간])
                start_end_date_arr.append([str(idx + 1), start_year + start_month + start_day, start_hour, end_year + end_month + end_day, end_hour])

            
            # zip과정에서 손실된 999개 이하의 시간들에 대해서 추가해주는 작업
            if start_end_date_arr[-1][3] + start_end_date_arr[-1][4] != (PastWeather.now - PastWeather.oneday).strftime('%Y%m%d') + "23":
                start_date = timestamp[999*(loopCount-1)]
                start_year = str(start_date.year)
                start_month = '0' + str(start_date.month) if len(str(start_date.month)) < 2 else str(start_date.month)
                start_day = '0' + str(start_date.day) if len(str(start_date.day)) < 2 else str(start_date.day)
                start_hour = '0' + str(start_date.hour) if len(str(start_date.hour)) < 2 else str(start_date.hour)

                start_end_date_arr.append([str(loopCount), start_year + start_month + start_day, start_hour, (PastWeather.now - PastWeather.oneday).strftime('%Y%m%d'), "23"])

        return start_end_date_arr


    def get_dataframe(self):
        # 호출기간별 시작날짜, 마지막날짜가 담긴 배열을 리턴하는 메서드 호출
        start_end_date_arr = PastWeather.get_start_end_date(self)

        weather_dataframe = pd.DataFrame(
            {'date': [], 'temp': [], 'rain': [], 'windspeed': [], 'humidity': [], 'atmos_pressure': [], 'daylight_hr': [], 'solar_insolation': [], 'cloud': []}
            )
        for period in start_end_date_arr:
            url_xml = str(PastWeather.url +
                          '?serviceKey=' + PastWeather.serviceKey +
                          '&pageNo=' + period[0] +
                          '&numOfRows=' + str(999) +
                          '&dataCd=' + PastWeather.dataCd +
                          '&dateCd=' + PastWeather.dateCd +
                          '&stnIds=' + self.stnIds +
                          '&startDt=' + period[1] +
                          '&startHh=' + period[2] +
                          '&endDt=' + period[3] +
                          '&endHh=' + period[4])

            response = urllib.request.urlopen(url_xml)
            response_code = response.getcode()

            if response_code == 200:
                response_body = response.read().decode('utf-8')  # decode('utf-8') : 바이트열 -> 문자열(복호화)
                soup = BeautifulSoup(response_body, 'html.parser')  # xml도 가능

                dataList = soup.find_all('item')
                for data in dataList:
                    new_row = pd.DataFrame(
                        {'date': [data.tm.text],
                        'temp': [data.ta.text],
                        'rain': [data.rn.text],
                        'windspeed': [data.ws.text],
                        'humidity': [data.hm.text],
                        'atmos_pressure': [data.pa.text],
                        'daylight_hr': [data.ss.text],
                        'solar_insolation': [data.icsr.text],
                        'cloud': [data.dc10tca.text]}
                        )

                    weather_dataframe = pd.concat([weather_dataframe, new_row], axis=0, ignore_index=True)

            else:
                print("response_code:", response_code)

            # 진행상황
            print('완료한 날짜:', period[3])

        # convert data type
        weather_dataframe['date'] = pd.to_datetime(weather_dataframe['date'], format="%Y-%m-%d %H:%M")
        weather_dataframe['temp'] = pd.to_numeric(weather_dataframe['temp'])
        weather_dataframe['rain'] = pd.to_numeric(weather_dataframe['rain'])
        weather_dataframe['windspeed'] = pd.to_numeric(weather_dataframe['windspeed'])
        weather_dataframe['humidity'] = pd.to_numeric(weather_dataframe['humidity'])
        weather_dataframe['atmos_pressure'] = pd.to_numeric(weather_dataframe['atmos_pressure'])
        weather_dataframe['daylight_hr'] = pd.to_numeric(weather_dataframe['daylight_hr'])
        weather_dataframe['solar_insolation'] = pd.to_numeric(weather_dataframe['solar_insolation'])
        weather_dataframe['cloud'] = pd.to_numeric(weather_dataframe['cloud'])

        return weather_dataframe

# # Test Call
# cls_instance = PastWeather('20201215', '108')
# dataframe = cls_instance.get_dataframe()
# print(dataframe)