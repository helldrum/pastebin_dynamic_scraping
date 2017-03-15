#!venv/bin/python
#coding:utf8

from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import re

search = "python"
url = "https://www.google.fr/?gfe_rd=cr&ei=S4rJWPnnHcWEaNjju7AH&gws_rd=ssl#q=site:pastebin.com+" + search + "&*"

browser = webdriver.Firefox()
browser.get(url)
time.sleep(5)
suffix_clean = []

soup = BeautifulSoup(browser.page_source, 'html.parser')
for link in soup.find_all('cite'):
  pastebin_suffix = link.string.split("/",1)[1]
  if re.search('([A-Za-z0-9]){8}', pastebin_suffix):
    suffix_clean.append(pastebin_suffix)

for suffix in suffix_clean:
  print suffix

#print ""
#print ""

#browser.get(url + "&start=10")

#time.sleep(4)

#soup = BeautifulSoup(browser.page_source, 'html.parser')
#for link in soup.find_all('a'):
#    print(link.string, link.get('href'))

