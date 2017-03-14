# venv/bin/python

from bs4 import BeautifulSoup
import requests
 
#url = input('Enter a website to extract URL\'s from: ')
r = requests.get('http://pastebin.com/archive')
 
data = r.text
 
soup = BeautifulSoup(data, 'html.parser')
 
for link in soup.find_all('a'):
    print(link.string, link.get('href'))
