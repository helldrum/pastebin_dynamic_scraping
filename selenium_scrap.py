#!venv/bin/python
#coding:utf8

from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import re
import requests

def scrap_pastebin_suffix( browser, suffix_clean):
  ## scrap and extract pastebin suffix ex pastebin.com/e2tYTu45 -> e2tYTu45
  soup = BeautifulSoup(browser.page_source, 'html.parser')
  for link in soup.find_all('cite'):
    pastebin_suffix = link.string.split("/",1)[1]
    if re.search('([A-Za-z0-9]){8}', pastebin_suffix):
      suffix_clean.append(pastebin_suffix)

def prepare_pastebin_raw_links(suffix_clean, pastebin_raw): 
  for suffix in suffix_clean:
    pastebin_raw.append("http://pastebin.com/raw/" + suffix)


#TODO main function + opt parser

search = "python"
page = 0
url = "https://www.google.fr/?gfe_rd=cr&ei=S4rJWPnnHcWEaNjju7AH&gws_rd=ssl#q=site:pastebin.com+" + search + "&start="
suffix_clean = []
pastebin_raw = []

#init selenium driver
browser = webdriver.Firefox()
 
time.sleep(5)
browser.get(url)
scrap_pastebin_suffix(browser, suffix_clean)



## TODO need to find a way to stop and save when google capcha gotcha
#while true:

  page += 10

  browser.get(url+str(page))
  time.sleep(10)
  scrap_pastebin_suffix(browser, suffix_clean)

prepare_pastebin_raw_links(suffix_clean, pastebin_raw)

## TODO print in a file or in terminal the good stuff :)
