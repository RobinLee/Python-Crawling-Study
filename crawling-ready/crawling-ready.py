#!/usr/local/bin/python3
#-*-coding: utf-8-*-

# import 할 플러그인을 불러옴 
#bs4라는 패키지에서 BeautifulSoup 플러그인 로드 
#통상 pip 명령어를 통해 설치함 (터미널창에서 설치 - 설치방법은...개별적으로 파악)
from bs4 import BeautifulSoup 
#URL을 불러오기 위한 플러그인 python3.x 버전에서는 기본설치 되어 있음 
import requests

#가져올 URL을 importURL이라는 변수에 저장 (여기서는 네이버의 많이본 연애 랭킹뉴스)
importUrl = 'https://entertain.naver.com/ranking'

#importURL 주소에 데이터를 요청하고 받은 내용을 source_code라는 변수에 text로 저장 
source_code = requests.get(importUrl).text

#source_code의 text 내용을 BeautifulSoup 플러인을 통해서 html로 파싱해서 soup 이라는 변수에 저장 
soup = BeautifulSoup(source_code, 'html.parser')

#html 파일내용 중 연애뉴스 리스트가 시작되는 ul 태그를 선택해서 가져옴  
my_titles_ul = soup.find("ul", {"id":"ranking_list"})

#가져온 ul 태그에서 li 태그를 모두 배열형태로 저장   
my_titles = my_titles_ul.find_all("li")

#해당 배열 변수를 출력 
print(my_titles)