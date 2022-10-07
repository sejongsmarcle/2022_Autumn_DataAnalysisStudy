import re
from bs4 import BeautifulSoup 
# 라이브러리에서 필요한 모듈을 불러온다.

html = open("css01.html","r",encoding="utf-8")
# css01.html 파일을 utf-8형태로 인코딩
soup=BeautifulSoup(html, "html.parser")
#soup를 html파일을 저장할 객체로 지정

h1 = soup.select_one('div#main-goods > h1').string 
print("h1 =",h1)
#div 태그중 main-goods인 항목을 h1태그의 문자열로 저장하고 출력하기

li_list = soup.select("div#main-goods > ul#fruits > li")
for li in li_list:
    print("li =",li.string)
       
#li_list에 div 태그중 main-goods인 항목중 fruits항목을 저장하고 
#문자열 형태로 출력하기
