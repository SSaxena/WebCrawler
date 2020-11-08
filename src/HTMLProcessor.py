import datetime
from collections import Counter
from bs4 import BeautifulSoup
import os
import csv


# extract all words from HTML and calculate the top 10 words
# The Top 10 Words on each Page are stored in CSV wrt to each Web Page URL
class HTMLProcessor:
    url = ''
    page = ''

    # CSV File name using the date format
    date = datetime.datetime.now()
    csvfilename = ''

    def __init__(self, pageurl):
        self.url = pageurl

    #
    def __init__(self, pageurl, pagedoc, filename):
        self.url = pageurl
        self.page = pagedoc
        # csv file name initialized once
        self.csvfilename = 'web-{year}-{month}-{day}-{min}'.format(year=self.date.year, month=self.date.month,
                                                                   day=self.date.day,
                                                                   min=self.date.minute)

    # Word Frequency counter after crawling a web-page

    # Function defining the web-crawler,
    # which will fetch information from
    # a given website, and push the contents to
    # the second function clean_wordlist()'''
    def startcounting(self):

        # empty list to store the contents of
        # the website fetched from our web-crawler
        wordlist = []

        soup = BeautifulSoup(self.page, 'html.parser')

        # Text in given web-page get the words and add into an collection
        content = soup.find().getText()
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        self.clean_wordlist(wordlist)

    # Function removes any unwanted symbols
    def clean_wordlist(self, wordlist):

        clean_list = []
        for word in wordlist:
            symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '

            for i in range(0, len(symbols)):
                word = word.replace(symbols[i], '')

            if len(word) > 0:
                clean_list.append(word)
        self.create_dictionary(clean_list)

    # Creates a dictionary containing each word's

    # count and top_20  words and store with URL
    def create_dictionary(self, clean_list):
        word_count = {}
        word_count2 = {}

        for word in clean_list:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        count = 0

        for word2 in clean_list:
            word2 = self.listToString(clean_list[count:count + 2])
            if word2 in word_count2:
                word_count2[word2] += 1
            else:
                word_count2[word2] = 1
            count += 1

        ''' To get the count of each word in 
            the crawled page --> 
        <-- '''

        c = Counter(word_count)
        c2 = Counter(word_count2)

        # returns the most occurring elements
        top = c.most_common(10)
        top2 = c2.most_common(10)
        self.fileWriter(top)
        self.fileWriter(top2)

    # To convert a list to string
    # Function to convert
    def listToString(self, s):
        # initialize an empty string
        str1 = ""

        # traverse in the string
        for ele in s:
            str1 += ele

        # return string
        return str1

    # Writing the data to csv file
    def fileWriter(self, inputString):
        cwd = os.getcwd()
        with open(f"{cwd}/{self.csvfilename}.csv", 'a') as out_file:
            writer = csv.writer(out_file)
            writer.writerow([self.url, inputString])
