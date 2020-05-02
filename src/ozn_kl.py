
import src.isfreader as isfr
import src.filter_butter as flt
import matplotlib.pyplot as plt
import numpy as np


string_name = "data\\tek0016"

data1 = isfr.read_file(string_name + "CH1.ISF")
t1 = data1[:, 0]
u1 = data1[:, 1]
# data2 = isfr.read_file(string_name + "CH2.ISF")
# t2 = data2[:, 0]
# u2 = data2[:, 1]
# data3 = isfr.read_file(string_name + "CH3.ISF")
# t3 = data3[:, 0]
# u3 = data3[:, 1]
# data4 = isfr.read_file(string_name + "CH4.ISF")
# t4 = data4[:, 0]
# u4 = data4[:, 1]

delta_t = t1[1] - t1[0]
u1_filt = flt.butter(u1, 100e3, delta_t)

ind = np.where(t1 >= 5.5 / 1e3)
ind1 = ind[0]

plt.figure()
# plt.plot(t1*1e3, u1, 'y')
# plt.plot(t2*1e3, u2, 'g')
# plt.plot(t3*1e3, u3, 'r')
plt.plot(t1[ind1]*1e3, u1_filt[ind1], 'y')
plt.show()
