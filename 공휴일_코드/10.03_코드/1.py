from bs4 import BeautifulSoup  
# bs4라이브러리에서 BeautifulSoup 모듈 불러오기

html = open("css01.html","r",encoding="utf-8")
# css01.html 파일을 utf-8형태로 인코딩
soup=BeautifulSoup(html, "html.parser")
#soup를 html파일을 저장할 객체로 지정
title=soup.select_one("div#main-goods>h1")
#title에 select_one함수에 css에 인자인 div#main-goods>h1를 넣어
# 원하는 정보를 저장한다.
print("h1 = ", title.string)

print(soup.select("ul#vegatables>li[class='us']")[0].string)
print(soup.select("ul#vegatables>li[class='us']")[1].string)
