Introduction:
This projet as been initiate in order to scrap pastebin with the google research feature inplemented in the site.
The pastebin API don't allow research and flexible wait to scrape all the website data.
The website use javascript in order to refresh page content, that's why i use selenium in order to get the full DOM in a dynamic way.


required:
python selenium 
```
pip install selenium
```
geckodriver
```
get https://github.com/mozilla/geckodriver/releases/download/v0.13.0/geckodriver-v0.13.0-linux64.tar.gz          
tar -xvzf geckodriver-v0.13.0-linux64.tar.gz
chmod +x geckodriver
put geckodriver in your PATH or cp into /usr/bin
```

BeautifulSoup
```
pip install
```
