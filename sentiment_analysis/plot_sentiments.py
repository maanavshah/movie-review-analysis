from pylab import *
import csv

def extractMovieName():
    line=''
    with open("data/urls.csv") as read_url:
        reader = csv.reader(read_url)
        firstline = True
        for row in reader:
            if firstline:
                line = row[0]
                firstline = False
                break
        line = line.strip('https://')
        values = line.split('/')
        return values[2]


figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])
labels = []
fracs = []
explode=[]
url = extractMovieName()
f = open("output/map_reduce.out")
data = f.readlines()
for line in data:
    line = line.replace('\n', '')
    key, value = line.split('\t')
    if key == '0':
        labels.append('Negative')
    elif key == '1':
        labels.append('Somewhat Negative')
    elif key == '2':
        labels.append('Neutral')
    elif key == '3':
        labels.append('Somewhat Positive')
    elif key == '4':
        labels.append('Positive')
    explode.append(0.00000002)
    fracs.append(value)
f.close()
pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
title(url, bbox={'facecolor':'0.8', 'pad':5})
show()
savefig('output/sentiment_analysis.png', bbox_inches='tight')