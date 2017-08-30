# Hi Daniel,
#
# You'll be pleased to hear I've made good progress with some Python code :-)
# I've got it working so that it looks at a url for an app on itumes and produces a report with the number of ratings that app has received.
# What I don't know how to do, is to it so that instead of running it on just one url, it imports a list of urls and loops through the whole list, producing a report with one line for each url's number of ratings.
# I've highlighted in yellow my dummy code which is where I need your help! thanks!
#
# Raf

import numpy as np
import csv
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_urls = []
my_ratings = []

with open('podcast_urls.txt', 'r') as file:
    file_contents = file.read()
    my_urls_list = file_contents.split()
    for url in my_urls_list:
        my_urls.append(url)

for my_url in my_urls:
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    rating = page_soup.findAll("span",{"class":"rating-count"})[0]

    my_ratings.append(rating)

with open("itunes_report.csv", "a") as csv_file:
    headers = ["url", "ratings-count"]
    itunes_writer = csv.DictWriter(csv_file, fieldnames=headers)

    itunes_writer.writeheader()

    for index, rating in enumerate(my_ratings):
        url = my_urls[index]
        ratings_count = my_ratings[index].text

        print("url:", url)
        print("rating html fragment:", rating)
        print("ratings count:", ratings_count)
        print("")

        itunes_writer.writerow({"url": url , "ratings-count": ratings_count})
