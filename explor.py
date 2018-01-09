import numpy as np
import scipy
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib as plt
from sklearn.feature_extraction import text


class explor:
    data_arr = 4

    def __init__(self, arr):
        self.data_arr = arr

    def print_total(self):
        print("There are " + str(len(self.data_arr)) + " of twiites in are corupus")

    def print_gender(self, gen):
        count = 0
        for item in self.data_arr:
            tmp = self.data_arr[item]
            if ("target" in tmp) and (tmp["target"] == gen):
                count += 1
        print "There are " + str(count) + " of the gender " + gen + " in are data"

    def adder(self, arr, arradd):
        for tt in arradd:
            arr.append(tt)
        return arr

    def print_language_length(self, gen):
#        arr = ([])
        ss = " "
        aa = text.ENGLISH_STOP_WORDS
        aaa = ([])
        for tt in aa:
            aaa.append(tt)
        aaa = self.adder(aaa, ['world', 'really', 'way', 'going', 'll', 'best', 've', 'new', 'http', 'https', 'time', 'just', 'don', 'like', 'love', 'day', '__', 'know', 'people','think','got','good','make','want','need','amp'])
        for item in self.data_arr:
            tmp = self.data_arr[item]
            if ("target" in tmp) and (tmp["target"] == gen) and ("text" in tmp):
#                arr.append(tmp["text"])
                ss = ss + tmp["text"]
        arr = [ss];
        vectorizer = CountVectorizer(stop_words=aaa)
        X = vectorizer.fit_transform(arr)
        ans_arr = vectorizer.get_feature_names()
        print "In gender " + gen + " there are " + str(len(ans_arr)) + " wrods"
        d = pd.Series(X.toarray().flatten(), index=ans_arr).sort_values(ascending=False)
#        ax = d[:10].plot(kind='bar', figsize=(10,6), width=.8, fontsize=14, rot=45, title='Barack Obama Wikipedia Article Word Counts')
#        ax.title.set_size(18)
        print d[:10]

