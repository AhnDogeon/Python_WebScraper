import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    # indeed 검색했을 때, HTML가져오기
    result = requests.get(URL)
    # BS이용 HTML Parse
    soup = BeautifulSoup(result.text, 'html.parser')
    # page a가 div 내 class = pagination으로 되어있음(F12로 확인)
    pagination = soup.find("div", {"class":"pagination"})

    links = pagination.find_all('a')

    # pages가 list 이므로 for문 가능

    pages = []
    for link in links[:-1]:
    # 여기서 a 태그 안에 span이 하나라면 다음과 같이 안쓰고
    #pages.append(int(link.find('span').string))
    # 이렇게 써줘도 된다.
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_indeed_jobs(last_pages):
    jobs = []
    # for page in range(last_pages):
    result = requests.get(f'{URL}&start={0*LIMIT}')
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
    
    for result in results:
        # result는 일자리 목록
        # h2라는 항목에서 class title은 것들을 추려냄
        # 그 안에서 anchor이면서 string이 title인 것들을 추려냄
        title = result.find("h2", {"class": "title"}).find("a")["title"]
        company = result.find("span", {"class": "company"})
        company_anchor = company.find("a")

        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        company = company.strip()
        print(company)
    return jobs
