# movie-review-analysis
A social web mining application for sentiment analysis of movie reviews. It performs sentiment analysis on movie review using NoSQL database(cassandra) and machine learning (the random forest algorithm) to label phrases on a scale of five values - negative, somewhat negative, neutral, somewhat positive, positive.

Overview
--------
Sentiment analysis is a well-known task in the realm of natural language processing. Given a set of texts, the objective is to determine the polarity of that text. Sentiment analysis aims to uncover the attitude of the author on a particular topic from the written text. We expect the short comment to express succinctly and directly author’s opinion on certain topic. We focus on polarity i.e. whether the author expresses positive or negative opinion.

We use statistical methods to capture the elements of subjective style and the sentence polarity. Statistical analysis is done on the sentence level. We apply machine learning techniques to classify set of messages.

The scope and requirements of this project can be defined as follows:
- Providing a social web mining application by online retrieval of data (rotten tomatoes and imdb api)
- Machine Learning algorithm to provide analysis and mining of big data (the random forest algorithm)
- NoSQL database involvement for processing of big data (cassandra)
- Designing of an application interface for presenting the analysis performed on big data (matplotlib)

Description
-----------
Sentiment analysis on movie reviews helps to label phrases on a scale of five values: negative, somewhat negative, neutral, somewhat positive, positive. We web scrap the IMDb website to collect the user reviews for different movies, which makes provision for test data. We then apply random forest classifier algorithm on the procured dataset. In particular, ‘model2.json’ feeds a random forest classifier with a concatenation of different kinds of features.  The decision functions of set of SGDClassifiers (scikit-learn library) trained in a one-versus-others scheme using bag-of-words on the wordnet of the words in a phrase. The amount of "positive" and "negative" words in a phrase as dictated by the Harvard Inquirer sentiment lexicon. During prediction, it also checks for duplicates between the training set and the test set. The prediction of sentiments are then handlend by NoSQL database which yeilds to plot graphically the analysis of sentiments (matplotlib library).

Installation
------------

#### Installing java

	$ apt-get update
	$ sudo apt-get install -y software-properties-common
	$ add-apt-repository ppa:webupd8team/java  # install oracle java
	$ apt-get update
	$ apt-get install oracle-java9-installer  # you can choose any stable version of java

#### Setting up java

	$ java -version
	$ update-alternatives --config java
	$ nano /etc/environment  # set the JAVA_HOME variable
	$ JAVA_HOME="/usr/lib/jvm/java-9-oracle"  # JAVA_HOME="/your/java/installation-path"
	$ source /etc/environment
	$ echo $JAVA_HOME  # test that everything is done fine

#### Installing Cassandra DB

	$ echo "deb http://www.apache.org/dist/cassandra/debian 22x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
	$ echo "deb-src http://www.apache.org/dist/cassandra/debian 22x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
	$ gpg --keyserver pgp.mit.edu --recv-keys F758CE318D77295D
	$ gpg --export --armor F758CE318D77295D | sudo apt-key add -
	$ gpg --keyserver pgp.mit.edu --recv-keys 2B5C1B00
	$ gpg --export --armor 2B5C1B00 | sudo apt-key add -
	$ gpg --keyserver pgp.mit.edu --recv-keys 0353B12C
	$ gpg --export --armor 0353B12C | sudo apt-key add -
	$ sudo apt-get update
	$ sudo apt-get install cassandra
	$ sudo service cassandra status
	$ sudo nano +60 /etc/init.d/cassandra
	- Change line from CMD_PATT="cassandra.+CassandraDaemon" to CMD_PATT="cassandra"

You can also refer for https://www.digitalocean.com/community/tutorials/how-to-install-cassandra-and-run-a-single-node-cluster-on-ubuntu-14-04 installing cassandra in ubuntu

#### Installing python3-pip

	$ sudo apt-get update
	$ sudo apt-get install python3-pip
	$ python3 -m venv --without-pip venv
	$ source venv/bin/activate

#### Setting up requirements

	$ pip3 install -r docs/setup/requirements-dev.txt
	$ pip3 install -r docs/setup/requirements.txt

#### Setting up nltk

Change the current directory to home, as the nltk directory should be present in home directory

	$ cd
	$ python3
	>>> import nltk
	>>> nltk.download()

You need to have following nltk packages - corpora, taggers, tokenizers

#### Execute script

In order to run this, you should be inside current directory of movie-review-analysis

	$ python3 scripts/execute.py

Once, it successfully runs you can find the pie chart of sentiments generated in the output folder. You can check the output generated in https://github.com/maanavshah/movie-review-analysis/tree/master/output directory. Check out the https://github.com/maanavshah/movie-review-analysis/blob/master/output/sentiment_analysis.png for the final pie chart output.

Contributing
------------

Bug reports and pull requests are welcome on GitHub at https://github.com/maanavshah/movie-review-analysis. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

License
-------

The application is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
