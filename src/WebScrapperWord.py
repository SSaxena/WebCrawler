from bs4 import BeautifulSoup
import requests
import os
import sys
from HTMLProcessor import HTMLProcessor


# Class to extract to the fetch thw HTML from the URL
# HTML Links are extracted from each page and MAX depth input value
class WebScapperWord:
    # lists
    urls = []
    def __init__(self, url):
        self.urls = url


    # initiate process of web scrapping
    # input the site URL and Max depth
    def startprocess(self, site, max_traverse):
        self.scrape(site, max_traverse)

    # Scaping the Web Page recursive method to go to MAX depth coming from input
    def scrape(self, siteurl, max):
        try:
            # getting the request from url
            r = requests.get(siteurl)

            # converting the text
            beautifulDoc = BeautifulSoup(r.text, "html.parser")
            max -= 1

            if max >= 0:
                for new_url in beautifulDoc.find_all('a', href=True):
                    new_url = new_url.get('href')

                    if new_url.startswith("https://www.314e.com/"):
                        new_siteurl = new_url

                        if new_siteurl not in self.urls:
                            # calling it self
                            htmlwordprocessor = HTMLProcessor(new_siteurl, r.text, '')
                            htmlwordprocessor.startcounting()
                            self.urls.append(new_siteurl)
                            self.scrape(new_siteurl, max)
        except:
            print('An Error Exception', sys.exc_info()[0], "occurred.")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

