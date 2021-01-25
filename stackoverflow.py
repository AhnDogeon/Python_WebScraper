import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", class_ = "s-pagination").find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)

def extract_job(html):
    title = html.find("h2", {"class": "mb4"}).find("a")["title"]
    # recursive는 span 안에 span 이 있을 경우 계속 타고 들어가지 않게 한다. (제일 위에 것만 가져옴)
    company, location = html.find("h3", {"class": "fc-black-700"}).find_all("span", recursive = False)
    company, location = company.get_text(strip=True), location.get_text(strip=True)
    print(company)
    print(location)
    return {'title' : title}

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page + 1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class" : "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
