import requests
from bs4 import BeautifulSoup

# indeed 검색했을 때, HTML가져오기
indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
# BS이용 HTML Parse
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
# page a가 div 내 class = pagination으로 되어있음(F12로 확인)
pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all('a')

# pages가 list 이므로 for문 가능

pages = []
for link in links[:-1]:
    # 여기서 a 태그 안에 span이 하나라면 다음과 같이 안쓰고
    #pages.append(int(link.find('span').string))
    # 이렇게 써줘도 된다.
    pages.append(int(link.string))

pages = pages[:-1]
max_page = pages[-1]