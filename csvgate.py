import csv
import convertcolor as colovert

class csvclass:
    """class example"""
    i = 1234
    csv_file = None

    def train_build(self):
        train_data = {}
        input_file = csv.reader(open("file.csv"))
        print (input_file.next())
#        reader = csv.DictReader(csvfile)
        count = 0
#       print(reader)
        gg = "22.222"
        float(gg)
        for row in input_file:
            if not row[6] == "":
                cc = float(row[6])
                gen = row[5]
                if cc > 0.65 and (gen == "male" or gen == "female"):
                    count += 1
                    tmp = {}
                    tmp['target'] = gen
                    tmp_txt = unicode(row[19], errors='ignore')
                    tmp['text'] = tmp_txt
                    tmp['color1'] = row[13]
                    tmp['color11'] = self.colorcon.rgb(tmp['color1'])
                    tmp['color2'] = row[18]
                    tmp['color21'] = self.colorcon.rgb(tmp['color2'])
                    train_data[row[0]] = tmp
        return train_data

    def load_csv_file(self, path):
        self.file_path = path

    def __init__(self):
        self.colorcon = colovert.convertcolor()
        self.i = 12
