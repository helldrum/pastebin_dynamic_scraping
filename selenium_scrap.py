#!venv/bin/python
#coding:utf8

from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import re
import requests

import os, sys
from optparse import OptionParser

#def scrap_pastebin_suffix( browser, suffix_clean):
#  ## scrap and extract pastebin suffix ex pastebin.com/e2tYTu45 -> e2tYTu45
#  soup = BeautifulSoup(browser.page_source, 'html.parser')
#  for link in soup.find_all('cite'):
#    pastebin_suffix = link.string.split("/",1)[1]
#    if re.search('([A-Za-z0-9]){8}', pastebin_suffix):
#      suffix_clean.append(pastebin_suffix)
#
#def prepare_pastebin_raw_links(suffix_clean, pastebin_raw): 
#  for suffix in suffix_clean:
#    pastebin_raw.append("http://pastebin.com/raw/" + suffix)
#
#search = "onion"
#page = 80
#url = "https://www.google.fr/?gfe_rd=cr&ei=S4rJWPnnHcWEaNjju7AH&gws_rd=ssl#q=site:pastebin.com+" + search + "&start="
#suffix_clean = []
#pastebin_raw = []
#
##init selenium driver
#browser = webdriver.Firefox()
# 
#time.sleep(5)
#browser.get(url)
#time.sleep(3)
#
#scrap_pastebin_suffix(browser, suffix_clean)
#
#next_button_exist = browser.find_element_by_css_selector("#pnnext > span")
#
#while next_button_exist :
#
#  try:
#    next_button_exist = browser.find_element_by_css_selector("#pnnext > span")
#  except NoSuchElementException:
#    next_button_exist = None
#  
#  page += 10
#  browser.get(url+str(page)+"&filter=0")
#  print "browse"+ url+str(page)+"&filter=0"
#  time.sleep(30)
#  scrap_pastebin_suffix(browser, suffix_clean)
#  prepare_pastebin_raw_links(suffix_clean, pastebin_raw)
#
#  for raw in pastebin_raw:
#    print raw
#    
#    file = open("testfile.txt","a")
#    file.write("\n+++++++++++++++++++++++++"+raw+"%+++++++++++++++++++++\n")
#
#    try:
#      result = requests.get(raw)
#    except ConnectionError:
#      pass
#
#    time.sleep(10)
#
#    file.write(result.text.encode('ascii', 'ignore'))
#    file.write("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
#    file.close()
#
#  suffix_clean = []
#  pastebin_raw = []
#
class CleanPastebinLink:

  def __init__(self, link):
    if re.search('pastebin', link):
      pastebin_suffix = link.split("/",1)[1]
      if re.search('([A-Za-z0-9]){8}', pastebin_suffix):
        self.suffix = pastebin_suffix
      else:
        raise ValueError("link do not match a pastebin standalone link.")
    else:
      raise ValueError("link is not a pastebin link.")

  def get_raw_link(self):
   return "http://pastebin.com/raw/" + self.suffix

class GoogleQuery:
  def __init__(self, query, start=0):
    self.url_base = "https://www.google.fr/?gfe_rd=cr&ei=S4rJWPnnHcWEaNjju7AH&gws_rd=ssl#"

    if not query:
      raise ValueError("parameter query is empty.")
    self.compose_base = self.url_base + "q=" + query + "&start=" + str(start)   
  
  def get_url(self):
    return self.compose_base

class SeleniumFirefox:
  def __init__(self):
    pass  

def start():
  parser = OptionParser()
  usage = "usage: %prog [options] arg1 arg2"

  parser.add_option("-f", "--file", type="string",
    help="output file, if this arg is not provide, result will be print in stdout",
    dest="output_file", default=None)

  parser.add_option("-g", "--google_tempo", type="int",
    help="google tempo during scrap, default value 30",
    dest="google_tempo", default=30)

  parser.add_option("-p", "--pastebin_tempo", type="int",
    help="pastebin tempo during scrap, default value 10",
    dest="pastebin_tempo",default=10)

  options, arguments = parser.parse_args()

  pastebin = CleanPastebinLink("pastebin.com/M5TscYhs")

  print pastebin.get_raw_link()
  google = GoogleQuery("site:pastebin.com+onion", start=20)
  print google.get_url()

  #pastebin = CleanPastebinLink("pastebin.com/lol/tralala")


if __name__ == '__main__':
  start()
