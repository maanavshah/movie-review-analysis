from cassandra.cluster import Cluster


def aggregateSentiment():
	print("\nSUMMARISING GENERATED SENTIMENTS :: ")
	cluster = Cluster()
	session = cluster.connect('movie_reviews')
	for i in range(0,5):
		results = session.execute("SELECT movie_name FROM movie_reviews.movie_sentiment WHERE sentiment = %s ALLOW FILTERING" % (i))
		print("\nMovies with sentiment %d ::" % (i))
		for row in results:
			print("-",row[0])

aggregateSentiment()