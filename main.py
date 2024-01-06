import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.billboard.com/charts/hot-100/')
soup = BeautifulSoup(response.text, 'html.parser')
hit_song_titles = [title.get_text() for title in soup.select('h3')]
print(hit_song_titles)