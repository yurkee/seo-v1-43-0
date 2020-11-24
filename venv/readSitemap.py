from bs4 import BeautifulSoup
import urllib.request

def get_web_link_value():
    page = urllib.request.urlopen("https://v1-43-0.btclass.net/sitemap")
    contents = page.read()

    soup = BeautifulSoup(contents, "html.parser")

    print(soup.find_all('a',class_="site-link"))


get_web_link_value()