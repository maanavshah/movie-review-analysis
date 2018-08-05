import numpy
import re

from sklearn.linear_model import SGDClassifier
from sklearn.multiclass import fit_ovo
import nltk


class StatelessTransform:
    def fit(self, X, y=None):
        return self


class ExtractText(StatelessTransform):
    def __init__(self, lowercase=False):
        self.lowercase = lowercase

    def transform(self, X):
        it = (" ".join(nltk.word_tokenize(datapoint.phrase)) for datapoint in X)
        if self.lowercase:
            return [x.lower() for x in it]
        return list(it)


class ReplaceText(StatelessTransform):
    def __init__(self, replacements):
        self.rdict = dict(replacements)
        self.pat = re.compile("|".join(re.escape(origin) for origin, _ in replacements))

    def transform(self, X):
        if not self.rdict:
            return X
        return [self.pat.sub(self._repl_fun, x) for x in X]

    def _repl_fun(self, match):
        return self.rdict[match.group()]


class MapToSynsets(StatelessTransform):
    def transform(self, X):
        return [self._text_to_synsets(x) for x in X]

    def _text_to_synsets(self, text):
        result = []
        for word in text.split():
            ss = nltk.wordnet.wordnet.synsets(word)
            result.extend(str(s) for s in ss if ".n." not in str(s))
        return " ".join(result)


class Densifier(StatelessTransform):
    def transform(self, X, y=None):
        return X.todense()


class ClassifierOvOAsFeatures:
    def fit(self, X, y):
        self.classifiers = fit_ovo(SGDClassifier(), X, numpy.array(y), n_jobs=-1)[0]
        return self

    def transform(self, X, y=None):
        xs = [clf.decision_function(X).reshape(-1, 1) for clf in self.classifiers]
        return numpy.hstack(xs)
