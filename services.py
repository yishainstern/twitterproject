from sklearn.feature_extraction import text
class services:
    name = "sds"

    def adder(self, arr, arradd):
        for tt in arradd:
            arr.append(tt)
        return arr

    def get_stop_wrods(self):
        aa = text.ENGLISH_STOP_WORDS
        aaa = ([])
        for tt in aa:
            aaa.append(tt)
        aaa = self.adder(aaa, ['world', 'really', 'way', 'going', 'll', 'best', 've', 'new', 'http', 'https', 'time',
                               'just', 'don', 'like', 'love', 'day', '__', 'know', 'people', 'think', 'got', 'good',
                               'make', 'want', 'need', 'amp'])
        return aaa

    def __init__(self):
        self.name = "name"