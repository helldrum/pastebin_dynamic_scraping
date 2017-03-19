Introduction:
This projet as been initiate in order to scrap pastebin with the google research feature inplemented in the site.
The pastebin API don't allow research and flexible wait to scrape all the website data.
I choose to use selenium in order to simulate user trafic on google and a large temporisation in order to not get blocked by google capcha
that's why it's running low but you have the possibility to change the default temporisation values.

requirement:

you need to use a virtualenv called venv in order to run the script (shebang harcoded on the top of the script)
you may need to install pip and virtualenv

```
virtualenv venv
```

python selenium 
```
pip install selenium
```
geckodriver
```
get https://github.com/mozilla/geckodriver/releases/download/v0.13.0/geckodriver-v0.13.0-linux64.tar.gz          
tar -xvzf geckodriver-v0.13.0-linux64.tar.gz
chmod +x geckodriver
put geckodriver in your PATH variable or cp into /usr/bin
```

BeautifulSoup
```
pip install beautifulsoup4
```

usage:
```
Usage: selenium_scrap.py [options]

Options:
  -h, --help            show this help message and exit
  -t SEARCH_KEYWORD, --search_term=SEARCH_KEYWORD
                        search keyword mandatory parameter
  -f OUTPUT_FILE, --file=OUTPUT_FILE
                        output file, if this arg is not provide, result will
                        be print in stdout
  -g GOOGLE_TEMPO, --google_tempo=GOOGLE_TEMPO
                        google tempo during scrap, default value 30
  -p PASTEBIN_TEMPO, --pastebin_tempo=PASTEBIN_TEMPO
                        pastebin tempo during scrap, default value 10
  -s STARTER, --page-start=STARTER
                        google scrap starter page, default value 0 (first
                        page)
```
parameter --search_term is required
