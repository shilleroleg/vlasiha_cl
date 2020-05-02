"""
Фильтр Баттерворта 5-го порядка

Вход:
signal - фильтруемый сигнал;
cut_freq - частота среза
step - шаг по времени. step = t[1] - t[0]
filt_type - Тип фильтра. По умолчанию - нижних частот (low).
            Возможные значения: ‘lowpass’, ‘highpass’, ‘bandpass’, ‘bandstop’.

Возвращает:
numpy-столбец отфильтрованных значений
"""
from scipy import signal
import numpy as np


def butter(input_signal, cut_freq, step,  filt_type='low'):

    b, a = signal.butter(5, cut_freq*2*step, filt_type)
    output = signal.filtfilt(b, a, input_signal)

    return np.array(output).T
