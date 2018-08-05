#!/bin/bash
python sentiment_analysis/crawler.py & 
wait
python sentiment_analysis/generate_sentiments.py data/model2.json > output/sentiment.csv & 
wait
python sentiment_analysis/extract_sentiments.py & 
wait
python sentiment_analysis/load_sentiments.py & 
wait
python sentiment_analysis/map_reduce.py & 
wait
python sentiment_analysis/plot_sentiments.py & 
wait
python sentiment_analysis/show_sentiments.py & 
wait
python sentiment_analysis/mean_sentiments.py &
wait
python sentiment_analysis/transform_movies.py & 
wait