import sys
import os
from WebScrapperWord import WebScapperWord

#Entry Point for the program with input arguments
# URL : https://www.314e.com/
# max depth : 4
if __name__ == '__main__':
    maxdepth = 4
    url = "https://www.314e.com/"
    n = len(sys.argv)
    if n == 3:
        try:
            if url.startswith("https://www.") or url.startswith("http://www."):
                url = sys.argv[1]
            if(type(sys.argv[2]) == int):
                maxdepth = int(sys.argv[2])
        except:
            print('Invalid arguments', sys.exc_info()[0], " . PLeas provide the URL and max depth for crawling ")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

    print("Web Scraping will be on URL", url,  " with max depth ", maxdepth)

    webscrapperword = WebScapperWord([])
    webscrapperword.startprocess(url, maxdepth)
