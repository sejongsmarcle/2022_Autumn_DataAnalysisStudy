import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

'''
네이버 영화 랭킹 페이지인 https://movie.naver.com/movie/sdb/rank/rmovie.naver에 접속하여 각 태그들을 이행하여 Beautiful Soup 사용법을 간단히 숙지해 보도록 합니다.
영화 순위와 제목 변동에 대한 상태를 출력해봅니다.
또한, 변동된 순위를 '변동값'이라는 컬럼에 반영해봅니다.

urllib.request 라이브러리의 urlopen() 함수를 이용하여 응답(response) 객체를 구합니다.
BeautifulSoup 클래스의 생성자에 매개 변수로 입력하여 soup 객체를 생성합니다.
'''
# Tag 및 Tag Name 조회
url = "http://movie.naver.com/movie/sdb/rank/rmovie.naver"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser') #무엇을 위한 기능?

'''
div 태그중 class 속성의 값이 tit3인 항목들을 추출합니다.
영화 제목만 뽑아 내려면 <a> 태그를 찾은 다음 string 속성을 사용하면 됩니다.
'''
tags = soup.findAll('div', attrs={'class':'tit3'}) #어떤 값들을 리스트로 하는지 html 코드 보면서 의미하는 바 설명
print('-' * 30)
print( tags )
print('-' * 30)

print('\n영화 제목만 뽑아내기')
for tag in tags :
    # 하위 <a> 태그 아래의 글자 영역
    print(tag.a.string)  # text 속성도 동일한 결과를 보여 준다.

'''
각 영화 목록에 대한 세부 페이지로 이동하려면, <a> 태그의 'href' 속성 값을 읽어서, 접두사 url(url_header 변수) 문자열을 결합해야 합니다.
'''

print('\n앵커의 href 속성')
url_header = 'https://movie.naver.com'
for tag in tags:
    print('-' * 50)
    print(url_header + tag.a['href'])

'''
모든 'tr' 태그를 찾아서 mytrs 변수에 저장합니다.
for 반복문을 이용하여 totallist라는 리스트에 저장하도록 합니다.
반복문 내에서 순위(newno), 제목(title), 변동(up_down), 변동 값(change) 들을 모두 구한 다음, 튜플형 자료 구조로 만든 다음에 totallist라는 리스트에 계속 추가합니다.
'''
mytrs = soup.find_all('tr') #tr 태그에 해당하는 것들이 무엇인지 html 코드 보고 의미하는 바 설명
# print(len(mytrs))
# print(type(mytrs))

no = 0 #무엇을 위한 변수인지=>순서
totallist = []

for one_tr in mytrs :
#     print(one_tr)
#     print('@' * 30)

    title = ''
    up_down = ''
    mytd = one_tr.find('td', attrs={'class':'title'})
    if (mytd != None) :
        no += 1
        newno = str(no).zfill(2)  #zfill함수가 무엇인지.

        mytag = mytd.find('div', attrs={'class':'tit3'})
        title = mytag.a.string

        mytd = one_tr.select_one('td:nth-of-type(3)')
        myimg = mytd.find('img')
        if myimg.attrs['alt'] == 'up':
            up_down = '상승'
        elif myimg.attrs['alt'] == 'down':
            up_down = '강등'
        else :
            up_down = '불변'

        change = one_tr.find('td', attrs={'class':'range ac'})  #class 연속으로 2개 쓰는 게 무엇을 의미
        if change == None :
            pass
        else:
            change = change.string
            # print(newno + '/' + title + '/' + up_down + '/'  + change)
            totallist.append((newno, title, up_down, change))

'''
totallist 리스트 데이터를 DataFrame으로 변경합니다.
해당 DataFrame을 'naverMovie.csv'라는 파일 이름로 파일을 생성합니다.
'''
mycolumn = ['순위', '제목', '변동', '변동값']

myframe = DataFrame(totallist, columns = mycolumn)   #pandas 관련된 건 너무 자세하지 않아도 ㅇㅋ
filename = 'naverMovie.csv'
myframe.to_csv(filename, encoding='cp949', index=False)
print(filename, '으로 저장되었습니다.', sep='')
print('finished')
