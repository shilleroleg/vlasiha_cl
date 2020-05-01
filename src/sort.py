import time
import numpy as np


def bubble_sort(A):
    for _ in range(len(A) - 1):
        for k in range(len(A) - 1):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]


def count_sort(A):
    N = len(A)
    F = [0]*10
    for i in range(N):
        F[A[i]] += 1

    c = 0
    for k in range(len(F)):
        if F[k] > 0:
            for m in range(F[k]):
                A[c] = k
                c += 1


A = [5, 4, 3, 2, 1]
# bubble_sort(A)
count_sort(A)
print(A)

B = [1, 2, 3, 5, 1]
# bubble_sort(B)
count_sort(B)
print(B)

# num = 500
# C = np.random.rand(num)
# start_time = time.time()
# bubble_sort(C)
# print(time.time() - start_time)
# # print(C)
#
# C2 = np.random.rand(num)
# start_time2 = time.time()
# C2.sort()
# print(time.time() - start_time2)
# # print(C2)
