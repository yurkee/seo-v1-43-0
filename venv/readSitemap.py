from bs4 import BeautifulSoup
import urllib.request
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context

def get_web_link_value():
    page = urllib.request.urlopen("https://v1-43-0.btclass.net/sitemap")
    contents = page.read()

    soup = BeautifulSoup(contents, "html.parser")

    linkstr = soup.find_all('a', class_="site-link")
    # print(linkstr)
    for i in linkstr:
        print(i)
        # res = re.findall(r'<[/s/S]+href="(.*)">', i)
        # print(res)

get_web_link_value()