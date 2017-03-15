#/usr/bin/python
#coding:utf8

import dryscrape
from bs4 import BeautifulSoup

search="python"
url="https://www.google.com/#?q=site:pastebin.com+" + search + "&*"

session = dryscrape.Session()
session.visit(url)
response = session.body()
soup = BeautifulSoup(response, "lxml")

for link in soup.find_all('a'):
  print(link.string, link.get('href'))
