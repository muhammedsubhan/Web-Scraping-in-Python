import requests
from bs4 import BeautifulSoup

# url = "https://subhan.vercel.app/"
# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'lxml')
    
#     title = soup.title.string
#     print("Page Title:", title)

#     for link in soup.find_all('a'):
#         print("Link:", link.get('href'))
    
#     # link = soup.find_all('a')
    
#     # print(link)

   
#     sections = soup.find_all('section')
#     for section in sections:
#         print("Section content:", section.get_text(strip=True))
# else:
#     print(f"Failed to retrieve the website. Status code: {response.status_code}")


url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=fullstack&txtLocation=USA"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    
    jobs = soup.find('li',class_='clearfix job-bx wht-shd-bx')
    
    company_name = jobs.find('h3', class_='joblist-comp-name').text.strip()
    keySkills = jobs.find('div', class_='more-skills-sections').text.strip()

print(f"""
=======================================
          Job Details
=======================================
Company Name   : {company_name}
Required Skills: {keySkills}
=======================================
""")

