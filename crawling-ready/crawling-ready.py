#!/usr/local/bin/python3
#-*-coding: utf-8-*-

# import 할 플러그인을 불러옴 
#bs4라는 패키지에서 BeautifulSoup 플러그인 로드 
#통상 pip 명령어를 통해 설치함 (터미널창에서 설치 - 설치방법은...개별적으로 파악)
from bs4 import BeautifulSoup 
#URL을 불러오기 위한 selenium 플러그인 가져오기 (이번에 가져올 네이버 연애뉴스 랭킹은 자바스크립트로 동적생성되는 html
#따라서 단순한 requsets 플러그인으로는 해당 내용이 가져와지지 않으므로 selenium으로 가져옴
from selenium import webdriver

# selenium의 webdriver를 파이어폭스드라이버로 사용하기
# webdriver는 기본으로 파폭 드라이버가 있음
# 윈도우에서는 다른 방법으로 사용해야할 것임
driver = webdriver.Firefox()

#가져올 URL을 importURL이라는 변수에 저장 (여기서는 네이버의 많이본 연애 랭킹뉴스)
importUrl = 'https://entertain.naver.com/ranking'

#해당 URL 가져오기 (여기에서 아마 Firefox 브라우저가 실행될 것임) - 그리고 해당 내용 가져오기
driver.get(importUrl)

#importURL 주소에 데이터를 요청하고 받은 내용을 source_code라는 변수에 저장
source_code = driver.page_source

#source_code의 text 내용을 BeautifulSoup 플러인을 통해서 html로 파싱해서 soup 이라는 변수에 저장 
soup = BeautifulSoup(source_code, 'html.parser')

#html 파일내용 중 연애뉴스 리스트가 시작되는 태그를 선택해서 가져옴
my_titles_ul = soup.select('#ranking_list > li > div.tit_area > a')

#가져온 a 태그의 내용숫자 만큼 loop문을 돌림
for my_title in my_titles_ul:
    # a 태그의 텍스트를 가져옴
    my_title_text = my_title.get_text()
    # 가져온 텍스트를 뿌려줌
    print(my_title_text)

#selenium 드라이버 종료
driver.quit()