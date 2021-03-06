import argparse
import json
import csv
import sys
from sentiment_analysis.corpus import iter_corpus, iter_test_corpus
from sentiment_analysis.predictor import PhraseSentimentPredictor
import csv
from cassandra.cluster import Cluster
import os
import re
from collections import Counter
from pylab import *
    
def fix_json_dict(config):
    new = {}
    for key, value in config.items():
        if isinstance(value, dict):
            value = fix_json_dict(value)
        elif isinstance(value, str):
            if value == "true":
                value = True
            elif value == "false":
                value = False
            else:
                try:
                    value = float(value)
                except ValueError:
                    pass
        new[key] = value
    return new


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("filename")
    config = parser.parse_args()
    config = json.load(open(config.filename))

    predictor = PhraseSentimentPredictor(**config)
    predictor.fit(list(iter_corpus()))
    test = list(iter_test_corpus())
    prediction = predictor.predict(test)

    writer = csv.writer(sys.stdout)
    writer.writerow(("PhraseId", "Sentiment"))
    for datapoint, sentiment in zip(test, prediction):
        writer.writerow((datapoint.phraseid, sentiment))