import requests
from bs4 import BeautifulSoup
from splash import SplashSession

session = SplashSession(wait_time=3)
url = 'https://www.century21.com/real-estate/new-york-ny/LCNYNEWYORK/'
splash_url = f'http://localhost:8050/render.html?url=https://www.century21.com/real-estate/new-york-ny/LCNYNEWYORK/&wait=3'

response = session.get(splash_url)
html_content = response.text

# Saving the raw HTML to a file
with open("raw_html_data.html", "w") as file:
    file.write(html_content)

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# You can now perform further data extraction and processing as required.
