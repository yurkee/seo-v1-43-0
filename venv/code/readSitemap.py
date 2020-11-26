# coding=utf-8
from bs4 import BeautifulSoup
import urllib.request
import ssl

#解决访问https时不受信任SSL证书问题
ssl._create_default_https_context = ssl._create_unverified_context

def get_web_link_value():
    #打开URL地址，读取页面
    page = urllib.request.urlopen("https://v1-43-0.btclass.net/sitemap")
    contents = page.read()

    #将html解析存入定义的soup
    soup = BeautifulSoup(contents, "html.parser")

    # #查找符合<a>标签中含有class属性值为"site-link"的所有标签，并以列表形式保存
    # linkstr = soup.find_all('a', class_="site-link")
    # print(linkstr)

    #用字典的方式存储，从页面中读取的值和超链接
    stDict = {}
    for i in soup.find_all('a', class_='site-link'):
    #     print(i)
    #     res = re.search(r'\<(.*?)\>', i)
    #     # print(res)
    #     #获取标签<a>中，href的属性值
        myLink = i['href']
        #获取标签<a>的text
        myText = i.string
        Dict = {myText:myLink}
        stDict.update(Dict)
    # print(stDict)
    return stDict