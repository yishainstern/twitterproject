import csvgate as cs
import explor as ex
cc = cs.csvclass()
cc.load_csv_file('file.csv')
ans = cc.train_build()
pp = ex.explor(ans)
pp.print_total()
pp.print_gender("male")
pp.print_gender("female")
pp.print_language_length("male")
pp.print_language_length("female")
#fdd