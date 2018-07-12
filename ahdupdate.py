#!usr/bin/python
import urllib.request
from bs4 import BeautifulSoup
import os

# use beautiful soup to retrieve HTML from AHD website
# store data in a variable 'html'
# use beautifulsoup methods to find the appropriate data in the soup object
# (could be current count of tickets in TAC_MIS and MY_QUEUE)
# store this data in a text file
# re run program every minute or so?
# compare the number(s) in the text file to the most recent number retrieved
# if there is a discrepency, a new ticket had been createdself...
# ... send a desktop notification, 'AHD ticket has been added'

page = urllib.request.urlopen('http://example.com')
html = page.read();
print(html)
os.system("pause")































#
