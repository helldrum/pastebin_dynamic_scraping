#!venv/bin/python
#coding:utf8

from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import re
import requests

search = "python"
page = 0
url = "https://www.google.fr/?gfe_rd=cr&ei=S4rJWPnnHcWEaNjju7AH&gws_rd=ssl#q=site:pastebin.com+" + search + "&start="
suffix_clean = []
pastebin_raw = []

browser = webdriver.Firefox()

browser.get(url)
time.sleep(5)

## scrap and extract pastebin suffix ex pastebin.com/e2tYTu45 -> e2tYTu45
soup = BeautifulSoup(browser.page_source, 'html.parser')
for link in soup.find_all('cite'):
  pastebin_suffix = link.string.split("/",1)[1]
  if re.search('([A-Za-z0-9]){8}', pastebin_suffix):
    suffix_clean.append(pastebin_suffix)

#for suffix in suffix_clean:
#  pastebin_raw.append("http://pastebin.com/raw/" + suffix)

#for url in pastebin_raw:
#  print "\n+++++++++++++++++++++++++" + url + "+++++++++++++++++++++\n"
#  result = requests.get(url)
#  time.sleep(1)
#  print result.text.encode('ascii', 'ignore')
#  print "\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"


page += 10

browser.get(url+str(page))
time.sleep(2)

soup = BeautifulSoup(browser.page_source, 'html.parser')
for link in soup.find_all('cite'):
  pastebin_suffix = link.string.split("/",1)[1]
  if re.search('([A-Za-z0-9]){8}', pastebin_suffix):
    suffix_clean.append(pastebin_suffix)


for suffix in suffix_clean:
  pastebin_raw.append("http://pastebin.com/raw/" + suffix)

for link in pastebin_raw:
  print link
