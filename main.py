import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.empireonline.com/tv/features/best-tv-2023/')
soup = BeautifulSoup(response.text, 'html.parser')
titles = [title.text for title in soup.select('h2 strong')]
titles = titles[::-1]   # reverse the array

with open('movie_title.txt', 'a') as file:
    for title in titles:
        file.write(title)
        file.write('\n')
