import os
from cassandra.cluster import Cluster


def main():
	cluster = Cluster()
	session = cluster.connect('movie_reviews')
	session.execute("TRUNCATE TABLE movie_reviews.movie_sentiment ;")
	print("\nSENTIMENT ANALYSIS ON MOVIE REVIEWS (SAMR)\n")
	os.system("javac Samr.java")
	os.system("java Samr")
	for j in range(5):
		for i in range(5):
			os.system("./scripts/bash.sh")
		print("------------------------------------------------------------------------------------------------------------------------------------------------------\n")

		os.system("wait")
		os.system("python sentiment_analysis/aggregate_sentiments.py")
		print("\n")
	os.system("rm -rf Samr.class")
		
if __name__ == '__main__':
	main()