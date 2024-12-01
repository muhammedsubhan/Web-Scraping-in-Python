import requests
from bs4 import BeautifulSoup

url = "https://subhan.vercel.app/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.title.string
    print("Page Title:", title)

    for link in soup.find_all('a'):
        print("Link:", link.get('href'))

   
    sections = soup.find_all('section')
    for section in sections:
        print("Section content:", section.get_text(strip=True))
else:
    print(f"Failed to retrieve the website. Status code: {response.status_code}")
