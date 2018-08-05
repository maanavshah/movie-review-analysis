import csv
from cassandra.cluster import Cluster
import os

f = open('output/sentiment.csv')
csv_f = csv.reader(f)
cluster = Cluster()
session = cluster.connect('movie_reviews')
session.execute("TRUNCATE TABLE movie_reviews.sentiment_analysis ;")
for row in csv_f:
	if row[0] != 'PhraseId':
		#print("INSERT INTO sentiment_analysis (phraseid , sentiment ) VALUES ( '{}', '{}') ;".format(row[0],row[1]))
		session.execute("INSERT INTO sentiment_analysis (phraseid , sentiment ) VALUES ( '{}', '{}') ;".format(row[0],row[1]))
os.system("cqlsh -f scripts/cquery.txt > output/cquery.out")