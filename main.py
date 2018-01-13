import csvgate as cs
import explor as ex
import services as ser
import tfidfmodel as tf
import models as mod
import knn as kk
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
tf_buid = tf.tfidfmodel(ans, stop_wrods)
top = tf_buid.extractTf()
run_mod = mod.models(top[0], top[1], top[2], top[3], top[4])
run_mod.start()
kkk = kk.knn(ans);
kkk.runKNN()

#fdd