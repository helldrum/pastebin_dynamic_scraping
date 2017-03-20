#!venv/bin/python
# coding: utf8

from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import re
import requests
import os, sys
from optparse import OptionParser
import urllib

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class CleanPastebinLink:
  def __init__(self, link):
    if re.search('pastebin', link):
      pastebin_suffix = link.split("/",1)[1] 
      match = re.search('([A-Za-z0-9]){8}', pastebin_suffix)
      if match:
        self.suffix = match.group(0)
      else:
        raise ValueError("link do not match a pastebin standalone link.")
    else:
      raise ValueError("link is not a pastebin link.")

  def get_raw_link(self):
   return str("http://pastebin.com/raw/" + self.suffix)


class GoogleQuery:
  def __init__(self, query, start=0):
    self.url_base = "https://www.google.fr/?gfe_rd=cr&ei=S4rJWPnnHcWEaNjju7AH&gws_rd=ssl#"

    if not query:
      raise ValueError("parameter query is empty.")
    self.compose_base = self.url_base + "q=" + query + "&start=" + str(start)   
  
  def get_url(self):
    return self.compose_base

def print_output(link, result, output_file):
  if "Pastebin.com - Page Removed" not in result:

    output = u"""
      \n+++++++++++++++++++++++++{}+++++++++++++++++++++\n
      {}\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n
      """.format(link, result)
  
    if output_file:
      file = open(output_file,"a")
      file.write(output)
      file.close()
    else:
      print output

def start():
  parser = OptionParser()

  parser.add_option("-t", "--search_term", type="string",
    help="search keyword mandatory parameter",
    dest="search_keyword", default=None)

  parser.add_option("-f", "--file", type="string",
    help="output file, if this arg is not provide, result will be print in stdout",
    dest="output_file", default=None)

  parser.add_option("-g", "--google_tempo", type="int",
    help="google tempo during scrap, default value 30",
    dest="google_tempo", default=30)

  parser.add_option("-p", "--pastebin_tempo", type="int",
    help="pastebin tempo during scrap, default value 10",
    dest="pastebin_tempo",default=10)
  
  parser.add_option("-s", "--page-start", type="int",
    help="google scrap starter page, default value 0 (first page)",
    dest="starter", default=0)

  options, arguments = parser.parse_args()
  if not options.search_keyword:
    "Error:parameter search_keyword is required, exiting..."
    parser.print_help()
    exit()

  starter = options.starter * 10
  browser = webdriver.Firefox()
  time.sleep(5)# wait for firefox to run
  next_button_exist = True

  try:
    while next_button_exist :  
      google = GoogleQuery("site:pastebin.com+{}".format(
         urllib.quote_plus(
           options.search_keyword)),
           start=starter)

      browser.get(google.get_url())
      time.sleep(3) # wait for the page to be full loaded 

      soup = BeautifulSoup(browser.page_source, 'html.parser')
      for link in soup.find_all('cite'):
        try:
          pastebin = CleanPastebinLink(str(link))
        except ValueError:
          pass
        result = requests.get(pastebin.get_raw_link())
        print_output(str(link), result.text, options.output_file)
        time.sleep(options.pastebin_tempo)

      try:
        next_button_exist = browser.find_element_by_css_selector("#pnnext > span")
      except NoSuchElementException:
        next_button_exist = None

      starter += 10 # google pagination increment 10 by 10
      time.sleep(options.google_tempo)

  except KeyboardInterrupt:
    print "execution interrupt by user"
    print "research " + options.output_file + " end in page "+ str(starter/10)
    sys.exit(0)

if __name__ == '__main__':
  start()
