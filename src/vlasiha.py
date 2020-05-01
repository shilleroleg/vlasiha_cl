# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:49:47 2020

@author: sou
"""

import src.isfreader as isfr
import matplotlib.pyplot as plt
import numpy as np

num = 181
string_name = "data\\tek0" + str(num)

data1 = isfr.read_file(string_name + "CH1.ISF")
t1 = data1[:, 0]
u1 = data1[:, 1]
data2 = isfr.read_file(string_name + "CH2.ISF")
t2 = data2[:, 0]
u2 = data2[:, 1]
data3 = isfr.read_file(string_name + "CH3.ISF")
t3 = data3[:, 0]
u3 = data3[:, 1]

#
delta_t = t1[1] - t1[0]
t_before = 0.005e-3      # время до максимума
t_after = 0.015e-3       # время после максимума

n_before = int(t_before / delta_t)      # Точек до максимум
n_after = int(t_after / delta_t)        # Точек после максимума
# print(n_before, n_after)

# Уровень шума
noise_1 = max(u1[0:1000]) * 1.1
noise_2 = max(u2[0:1000]) * 1.1
noise_3 = max(u3[0:1000]) * 1.1
# print(noise_1)

# plt.figure()
# plt.plot(t1*1e3, u1+(noise_1+noise_2)*1.1, 'y',
#          t2*1e3, u2, 'g',
#          t3*1e3, u3-(noise_2+noise_3)*1.1, 'r')
# plt.show()

# Находим индексы, где амплитуда напряжения выше шума
ind = np.where(u1 >= noise_1)
ind1 = ind[0]
ind = np.where(u2 >= noise_2)
ind2 = ind[0]
ind = np.where(u3 >= noise_3)
ind3 = ind[0]
# print(ind1)
# print(t1[ind1]*1e3)
# print(u1[ind1])

# Фаза А
count = 0
prev_i = 0
for i in ind1:
    if count > 0 and i - prev_i < n_after:
        continue

    t_temp = t1[i-n_before:i+n_after]
    u1_temp = u1[i - n_before:i + n_after]
    u2_temp = u2[i - n_before:i + n_after]
    u3_temp = u3[i - n_before:i + n_after]
    count += 1
    prev_i = i

    plt.figure()
    plt.plot(t_temp*1e3, u1_temp+(noise_1+noise_2)*1.1, 'y',
             t_temp*1e3, u2_temp, 'g',
             t_temp*1e3, u3_temp-(noise_2+noise_3)*1.1, 'r')
    plt.savefig(string_name[5:] + "_fig_A_" + str(i))
    plt.close()
    # plt.show()

# Фаза B
count = 0
prev_i = 0
for i in ind2:
    if count > 0 and i - prev_i < n_after:
        continue

    t_temp = t2[i-n_before:i+n_after]
    u1_temp = u1[i - n_before:i + n_after]
    u2_temp = u2[i - n_before:i + n_after]
    u3_temp = u3[i - n_before:i + n_after]
    count += 1
    prev_i = i

    plt.figure()
    plt.plot(t_temp*1e3, u1_temp+(noise_1+noise_2)*1.1, 'y',
             t_temp*1e3, u2_temp, 'g',
             t_temp*1e3, u3_temp-(noise_2+noise_3)*1.1, 'r')
    plt.savefig(string_name[5:] + "_fig_B_" + str(i))
    plt.close()

# Фаза C
count = 0
prev_i = 0
for i in ind3:
    if count > 0 and i - prev_i < n_after:
        continue

    t_temp = t3[i-n_before:i+n_after]
    u1_temp = u1[i - n_before:i + n_after]
    u2_temp = u2[i - n_before:i + n_after]
    u3_temp = u3[i - n_before:i + n_after]
    count += 1
    prev_i = i

    plt.figure()
    plt.plot(t_temp*1e3, u1_temp+(noise_1+noise_2)*1.1, 'y',
             t_temp*1e3, u2_temp, 'g',
             t_temp*1e3, u3_temp-(noise_2+noise_3)*1.1, 'r')
    plt.savefig(string_name[5:] + "_fig_C_" + str(i))
    plt.close()
