import requests
from bs4 import BeautifulSoup

# Function to scrape article titles from the OpenAI blog
def scrape_blog_titles(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup.prettify())
        titles = soup.find_all('h1', class_='h2')
        return [title.text.strip() for title in titles]
    else:
        print('Failed to fetch blog titles:', response.status_code)
        return None

# URL of the OpenAI blog
blog_url = 'https://openai.com/blog/'

# Scrape article titles from the OpenAI blog
blog_titles = scrape_blog_titles(blog_url)

if blog_titles:
    print('Blog Titles:')
    for title in blog_titles:
        print(title)
