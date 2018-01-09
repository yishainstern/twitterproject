import math


class tfidfmodel:
    main_source = None
    cleen_wrods = None
    max_index_for_train = 0
    test = {}
    train = {}

    def build(self):
        x = 5

    def __init__(self, source, wrods):
        self.cleen_wrods = wrods
        self.main_source = source
        self.max_index_for_train = (math.floor(len(self.main_source)/10))*9
        self.test['target_names'] = ['male', 'female']
        self.train['target_names'] = ['male', 'female']
        self.build()