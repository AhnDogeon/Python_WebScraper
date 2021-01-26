import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def get_last_page():
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

def extract_job(html):
    # h2라는 항목에서 class title은 것들을 추려냄
    # 그 안에서 anchor이면서 string이 title인 것들을 추려냄
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    if company:
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        company = company.strip()
    else:
        company = None
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {"title": title, "company": company, "location": location,
    "link": f"https://www.indeed.com/viewjob?jk={job_id}"}

def extract_jobs(last_pages):
    jobs = []
    for page in range(last_pages):
        print(f"Scrapping page {page}")
        result = requests.get(f'{URL}&start={page*LIMIT}')
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
        
        for result in results:
            # result는 일자리 목록
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs

