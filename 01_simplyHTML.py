from urllib.request import urlopen
from bs4 import BeautifulSoup

# 访问网页 html.read() 可以获取网页的 html文本
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# html.parser 按照 html文本 解析获取到的内容
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)

# <h1>An Interesting Title</h1>

bs1 = BeautifulSoup(html.read(), 'lxml')
print(bs1)

bs2 = BeautifulSoup(html.read(), 'html5lib')
print(bs2)