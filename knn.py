import pandas as pd
import math
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class knn:
    data = {}
    train_arr_data = []
    train_arr_target = []
    end_train_arr_data = []
    end_train_arr_target = []
    test_arr_data = []
    test_arr_target = []
    part = 10
    mod = None

    def runKnnOnTwiit(self, twitarr, file_input):
        self.test_arr_data = ([])
        countt = 0
        for item in twitarr:
            tmp_item = twitarr[item]
            if countt > 0:
                if tmp_item['color11']:
                    if (not (tmp_item['color11'][0] == -10)) and (not (tmp_item['color11'][1] == -10)) and (not (tmp_item['color11'][2] == -10)):
                        tmp_arr = [tmp_item['color11'][0], tmp_item['color11'][1], tmp_item['color11'][2]]
                        self.test_arr_data.append(tmp_arr)
                if tmp_item['color21']:
                    if (not (tmp_item['color21'][0] == -10)) and (not (tmp_item['color21'][1] == -10)) and (not (tmp_item['color21'][2] == -10)):
                        tmp_arr = [tmp_item['color21'][0], tmp_item['color21'][1], tmp_item['color21'][2]]
                        self.test_arr_data.append(tmp_arr)
            else:
                countt = 1
        iris_pred = self.mod.predict(self.test_arr_data)
        print "for file: " + file_input + " there are " + str(len(iris_pred)) + " rows."
        count0 = 0
        count1 = 0
        for tt in iris_pred:
            if tt == 0:
                count0 += 1
            elif tt == 1:
                count1 += 1
        pre = int(math.floor(100 * (float(count0)/float(len(iris_pred)))))
        print("there are " + str(count0) + " man which are " + str(pre) + "%")
        pre = int(math.floor(100 * (float(count1) / float(len(iris_pred)))))
        print("there are " + str(count1) + " woman which are " + str(pre) + "%")
    def runKNN(self):
        self.mod = KNeighborsClassifier(n_neighbors=14, algorithm='brute', p=1)
        self.mod.fit(self.end_train_arr_data, self.end_train_arr_target)
        iris_pred = self.mod.predict(self.test_arr_data)
        print "SCORE OF ACCURACY OF KNN"
        print(accuracy_score(self.test_arr_target, iris_pred))

    def build(self):
        for item in self.data:
            tmp = self.data[item]
            if tmp['target']=="male":
                tmp_tar = 0
            else:
                tmp_tar = 1
            if tmp['color11']:
                if (not (tmp['color11'][0] == -10)) and (not (tmp['color11'][1] == -10)) and (not (tmp['color11'][2] == -10)):
                    tmp_arr = [tmp['color11'][0], tmp['color11'][1], tmp['color11'][2]]
                    self.train_arr_data.append(tmp_arr)
                    self.train_arr_target.append(tmp_tar)
            if tmp['color21']:
                if (not (tmp['color21'][0] == -10)) and (not (tmp['color21'][1] == -10)) and (not (tmp['color21'][2] == -10)):
                    tmp_arr = [tmp['color21'][0], tmp['color21'][1], tmp['color21'][2]]
                    self.train_arr_data.append(tmp_arr)
                    self.train_arr_target.append(tmp_tar)
        self.max_index_for_train = (math.floor(len(self.train_arr_data) / self.part)) * (self.part - 1)
        print "size of data:" + str(len(self.train_arr_data))
        print "size of train: " + str(self.max_index_for_train)
        print "size of test: " + str(len(self.train_arr_data) - self.max_index_for_train)
        for i in range(0, len(self.train_arr_data)):
            tt = self.train_arr_data[i]
            ttt = self.train_arr_target[i]
            if i <= self.max_index_for_train:
                self.end_train_arr_data.append(tt)
                self.end_train_arr_target.append(ttt)
            else:
                self.test_arr_data.append(tt)
                self.test_arr_target.append(ttt)

    def __init__(self, train):
        self.data = train
        self.train_arr_data = ([])
        self.train_arr_target = ([])
        self.end_train_arr_data = ([])
        self.end_train_arr_target = ([])
        self.test_arr_data = ([])
        self.test_arr_target = ([])
        self.build()

