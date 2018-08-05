import urllib.request
from bs4 import BeautifulSoup
import csv
import signal
import sys
import re

signal.signal(signal.SIGINT, lambda x,y: sys.exit(0))

with open('data/urls.csv','r') as f:
	reader = csv.reader(f)
	rt_urls = list(reader)

def get_sentiment(rating):
	if rating < 20:
		return 0
	elif rating >= 20 and rating < 40:
		return 1
	elif rating >= 40 and rating < 60:
		return 2
	elif rating >= 60 and rating < 80:
		return 3
	else:
		return 4

csvfile = open('data/traindata.csv','w')

#reviews taken only from Inception for now
URL = 'http://www.metacritic.com/movie/inception/critic-reviews'
hdr = {'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request(URL,headers=hdr)
content = urllib.request.urlopen(req)

soup = BeautifulSoup(content, "html.parser")

reviews = soup.findAll("a", { "class" : "no_hover" })
scores = soup.findAll("div",{"class" : lambda x: x and x.startswith('metascore_w')})
scores = scores[4:]
for review,score in zip(reviews,scores):
	wr = csv.writer(csvfile,dialect='excel')
	wr.writerow([review.text.encode('utf-8')]+[str(get_sentiment(int(score.text)))])