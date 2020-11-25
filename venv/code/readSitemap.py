# coding=utf-8
from bs4 import BeautifulSoup
import urllib.request
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context

def get_web_link_value():
    page = urllib.request.urlopen("https://v1-43-0.btclass.net/sitemap")
    contents = page.read()

    soup = BeautifulSoup(contents, "html.parser")

    # linkstr = soup.find_all('a', class_="site-link")
    # print(linkstr)
    stDict = {}
    for i in soup.find_all('a', class_='site-link'):
        # print(i)
        # res = re.search(r'\<(.*?)\>', i)
        # print(res)
        myLink = i['href']
        myText = i.string
        Dict = {myText:myLink}
        stDict.update(Dict)
    # print(stDict)
    return stDict