# cython: language_level=3
# distutils: define_macros=NPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION
# distutils: extra_compile_args = -fopenmp
# distutils: extra_link_args = -fopenmp
# soma_paralela.pyx
import numpy as np
cimport numpy as np
cimport cython
from cython.parallel import prange

# Versão sequencial
@cython.boundscheck(False)
@cython.wraparound(False)
def soma_sequencial(np.ndarray[np.int64_t] arr):
    cdef long long total = 0
    cdef int i
    for i in range(arr.shape[0]):
        total += arr[i]
    return total

# Versão paralela com OpenMP
@cython.boundscheck(False)
@cython.wraparound(False)
def soma_paralela(np.ndarray[np.int64_t] arr, int num_threads=4):
    cdef long long total = 0
    cdef int i
    for i in prange(arr.shape[0], nogil=True, num_threads=num_threads):
        total += arr[i]
    return total