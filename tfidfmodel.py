from __future__ import print_function
import sys, os, time
import math
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import logging
import numpy as np
import sys
from time import time
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.utils.extmath import density
from sklearn import metrics


class tfidfmodel:
    main_source = None
    cleen_wrods = None
    max_index_for_train = 0
    test = {}
    train = {}
    part = 10

    def ad_to_diction(self, item, diction ):
        ps = PorterStemmer()
        tmp_str = item['text']
        words = nltk.tokenize.word_tokenize(tmp_str)
        str_ans = ""
        for word in words:
            if word not in self.cleen_wrods:
                word = word.lower()
                word = ps.stem(word)
                word = word.strip()
                str_ans += word + " "
        diction['target'].append(item['target'])
        diction['data'].append(str_ans.strip())

    def build(self):
        x = 5
        count = 0
#        for i in range(len(self.main_source)):
        for i in self.main_source:
            tmp = self.main_source[i]
            if count <= self.max_index_for_train:
                diction = self.train
            else:
                diction = self.test
            self.ad_to_diction(tmp, diction)
            count += 1

    def extractTf(self):
        target_names = self.test['target_names']
        # split a training set and a test set
        train_target, test_target = self.train['target'], self.test['target']
        t0 = time()
        top1 = (1, 2)
        print("Extracting features from the training data using a sparse vectorizer")
        vectorizer = TfidfVectorizer(sublinear_tf=True, stop_words='english', ngram_range=top1,max_df=0.6)
        train_idf = vectorizer.fit_transform(self.train['data'])
        print("n_samples: %d, n_features: %d" % train_idf.shape)
        print()

        print("Extracting features from the test data using the same vectorizer")
        t0 = time()
        test_idf = vectorizer.transform(self.test['data'])
        print("n_samples: %d, n_features: %d" % test_idf.shape)
        print()
        return target_names, train_target, test_target, train_idf, test_idf

    def __init__(self, source, wrods):
        self.cleen_wrods = wrods
        self.main_source = source
        self.max_index_for_train = (math.floor(len(self.main_source)/self.part))*(self.part-1)
        self.test['target_names'] = ['male', 'female']
        self.train['target_names'] = ['male', 'female']
        self.train['data'] = ([])
        self.test['data'] = ([])
        self.train['target'] = ([])
        self.test['target'] = ([])
        self.build()
