import src.my_fft as mf
import src.csv_read as cr

[sig_t, sig_u] = cr.csv_read("fft_data//signal_test.dat", 2, 1)
[freq_test, ampl_test] = cr.csv_read("fft_data//fft_test.dat", 2, 1)

[freq, ampl] = mf.my_fft(sig_u, sig_t[1] - sig_t[0], 10e3)

ferr = []
aerr = []
step = 0
max_steps = len(freq)
while step < max_steps:
    ferr.append(abs(freq_test[step] - freq[step]))
    aerr.append(abs(ampl_test[step] - ampl[step]))
    step += 1

print(f"freq_test={len(freq_test)},  freq {len(freq)},  error {sum(ferr)}")
print(f"ampl_test={len(ampl_test)},  ampl {len(ampl)},  error {sum(aerr)}")

# print(f"ampl_test= {ampl_test[0:20]}")
# print(f"ampl= {ampl[0:20]}")
# print(freq[9998])
