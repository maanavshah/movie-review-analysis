from cassandra.cluster import Cluster
import csv 
def calculateTotalSentiment():
	with open("output/map_reduce.out","r") as sentiment_f:
		elements = []
		for line in sentiment_f:
			values = line.split('\t')
			elements.append(values)
		mean=0
		sum_freq=0
		sum_values=0
		for row in elements:
			sum_values += (int(row[0])+1)*int(row[1])
			sum_freq += int(row[1])
		mean = sum_values/sum_freq
		return mean-1

def extractMovieName():
	line=''
	with open("]data/urls.csv") as read_url:
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

def addToCassandra(mean,movie):
	cluster = Cluster()
	session = cluster.connect('movie_reviews')
	session.execute("CREATE TABLE IF NOT EXISTS movie_reviews.movie_sentiment ( movie_name text, sentiment int, PRIMARY KEY (movie_name,sentiment) );")
	session.execute("INSERT INTO movie_reviews.movie_sentiment (movie_name,sentiment) VALUES (%s,%s);", (movie,int(mean)))	

mean = calculateTotalSentiment()
movie_name = extractMovieName()
addToCassandra(mean,movie_name)
