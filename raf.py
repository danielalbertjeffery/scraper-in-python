import numpy as np
data= np.genfromtxt('URLs.txt', delimiter=',')

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

for each my_url in my_urls...
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

Ratings = page_soup.findAll("span",{"class":"rating-count"})
rating=Ratings[0]
filename = "itunes_report.csv"
f = open(filename, "w")
headers = "url, ratings-count\n"
f.write(headers)
f.write(my_url +  "," + rating.text)
f.close()
