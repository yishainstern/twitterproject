from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import MultinomialNB
import matplotlib.pyplot as plt
import logging
import numpy as np
import sys
from time import time
import matplotlib.pyplot as plt
from sklearn.utils.extmath import density
from sklearn import metrics
class models:
    names = None
    train_target = None
    test_target = None
    train_feachers = None
    test_feachers = None

    def trim(self, s):
        """Trim string to fit on terminal (assuming 80-column display)"""
        return s if len(s) <= 80 else s[:77] + "..."

    def __init__(self, arr , tar_tran, tar_test, vec_train, vec_test):
        self.name = arr
        self.train_target = tar_tran
        self.test_target = tar_test
        self.train_feachers = vec_train
        self.test_feachers = vec_test


    # #############################################################################
    # Benchmark classifiers
    def benchmark(self, clf):
        print('_' * 80)
        print("Training: ")
        print(clf)
        t0 = time()
        clf.fit(self.train_feachers, self.train_target)
        train_time = time() - t0
        print("train time: %0.3fs" % train_time)

        t0 = time()
        pred = clf.predict(self.test_feachers)
        test_time = time() - t0
        print("test time:  %0.3fs" % test_time)

        score = metrics.accuracy_score(self.test_target, pred)
        print("accuracy:   %0.3f" % score)

        print()
        clf_descr = str(clf).split('(')[0]
        return clf_descr, score, train_time, test_time

#    (SGDClassifier(loss="hinge", alpha=0.00005, fit_intercept=False), "SVM")
#    (Perceptron(class_weight="balanced",), "Perceptron")
#
    def start(self):
        results = []
        for clf, name in ((MultinomialNB(alpha=0.005), "Naive Bayes"),
                          (SGDClassifier(loss="hinge", alpha=0.00005, fit_intercept=False), "SVM"),
                          (Perceptron(class_weight="balanced", ), "Perceptron")):
            print('=' * 80)
            print(name)
            results.append(self.benchmark(clf))

            # make some plots

        indices = np.arange(len(results))

        results = [[x[i] for x in results] for i in range(4)]

        clf_names, score, training_time, test_time = results
        training_time = np.array(training_time) / np.max(training_time)
        test_time = np.array(test_time) / np.max(test_time)

        plt.figure(figsize=(12, 8))
        plt.title("Score")
        plt.barh(indices, score, .2, label="score", color='navy')
        plt.barh(indices + .3, training_time, .2, label="training time", color='c')
        plt.barh(indices + .6, test_time, .2, label="test time", color='darkorange')
        plt.yticks(())
        plt.legend(loc='best')
        plt.subplots_adjust(left=.25)
        plt.subplots_adjust(top=.95)
        plt.subplots_adjust(bottom=.05)

        for i, c in zip(indices, clf_names):
            plt.text(-.3, i, c)
