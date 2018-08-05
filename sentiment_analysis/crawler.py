import urllib.request
from bs4 import BeautifulSoup
import csv
import signal
import sys
from subprocess import call
import os

signal.signal(signal.SIGINT, lambda x,y: sys.exit(0))

with open('data/urls.csv','r') as f:
	reader = csv.reader(f)
	rt_urls = list(reader)

csvfile = open('data/test.tsv','w')
wr = csv.writer(csvfile,dialect='excel',delimiter='\t')
wr.writerow(["PhraseId","SentenceId","Phrase"])

for i in rt_urls:	
	count = 0
	print("------------------------------------------------------------------------------------------------------------------------------------------------------\n")
	print("Fetching movie reviews :: ",i,"\n")
	URL = "".join((str(i).replace('[','').replace(']','').replace("'",""),'reviews'))
	url = urllib.request.urlopen(URL)
	content = url.read()
	soup = BeautifulSoup(content,"html.parser")
	mydivs = soup.findAll("div", { "class" : "the_review" })
	temp_id = 15601
	for i in mydivs:
		review = str(i).replace('<div class="the_review">','').replace('</div>','').lstrip()
		review = review.replace('\n', ' ').replace('\r', '')
		if review != "":
			print("-",review)
			wr.writerow([temp_id,temp_id,str(review)])
			temp_id = temp_id + 1
			count = count + 1
	print("\nTotal reviews fetched :: ", count,"\n")
	print("Performing sentiment analysis!\n")
	break