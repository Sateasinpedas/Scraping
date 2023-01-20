from bs4 import BeautifulSoup
import requests
import time


print('Put some skill that you are not familiar with')
unfamiliar_skills = input('>')
print(f'Filtering out {unfamiliar_skills}')

#import web
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ ='sim-posted').span.text
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
        skills = job.find('span', class_ ='srp-skills').text.replace(' ','')
        info = job.header.h2.a['href'] 
        if unfamiliar_skills not in skills:
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f"Company: {company_name.strip()}")
                f.write(f"Required Skills: {skills.strip()}")
                f.write(f'More info: {info}')
                print('')
            print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} seconds')
        time.sleep(time_wait * 60)
