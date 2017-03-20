#!/usr/bin/python
# coding: utf8

import re

def files():
n = 0
while True:
  n += 1
  yield open('%03d.part' % n, 'w')

fs = files()
outfile = next(fs) 

regex="\+{25}http:\/\/pastebin\.com\/raw\/[a-zA-Z0-9]{8}\%\+{21}"
with open("python.txt") as infile:
  for line in infile:
    if not re.split(regex, line):
      outfile.write(line)
    else:
      items = re.split(regex, line)
      outfile.write(items[0])
      for item in items[1:]:
        outfile = next(fs)
        outfile.write(item)
