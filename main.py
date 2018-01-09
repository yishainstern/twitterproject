import csvgate as cs
import explor as ex
import services as ser
cc = cs.csvclass()
ser = ser.services()
stop_wrods = ser.get_stop_wrods()
cc.load_csv_file('file.csv')
ans = cc.train_build()
pp = ex.explor(ans, stop_wrods)
pp.print_total()
pp.print_gender("male")
pp.print_gender("female")
pp.print_language_length("male")
pp.print_language_length("female")
#fdd