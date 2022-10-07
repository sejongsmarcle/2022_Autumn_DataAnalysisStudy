from urllib.request import urlopen
from bs4 import BeautifulSoup
# 라이브러리에서 필요한 모듈을 불러온다.


response = urlopen('https://music.bugs.co.kr/chart')
#벅스 링크를 urlopen 함수로 열기

soup = BeautifulSoup(response, 'html.parser')
#soup를 html파일을 저장할 객체로 지정
tags = soup.findAll('p', attrs={'class': 'title'}) 
#p태그 중 클래스 속성 값이 title인 항목 추출
i = 1
for tag in tags:
    print('%d위: %s' % (i, tag.a.string))
    i += 1
#반복문을 사용하여 <a>태그 영역에 문자를 몇 위 영화이름 형태에 맞춰 출력하기.    