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

    def runKNN(self):
        mod = KNeighborsClassifier(n_neighbors=14, algorithm='brute', p=1)
        mod.fit(self.end_train_arr_data, self.end_train_arr_target)
        iris_pred = mod.predict(self.test_arr_data)
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
        for i in range(0, len(self.train_arr_data)):
            tt = self.train_arr_data[i]
            ttt = self.train_arr_target[i]
            if i <= self.max_index_for_train:
                self.end_train_arr_data.append(tt)
                self.end_train_arr_target.append(ttt)
            else:
                self.test_arr_data.append(tt)
                self.test_arr_target.append(ttt)

    def __init__(self,train):
        self.data = train
        self.train_arr_data = ([])
        self.train_arr_target = ([])
        self.end_train_arr_data = ([])
        self.end_train_arr_target = ([])
        self.test_arr_data = ([])
        self.test_arr_target = ([])
        self.build()

