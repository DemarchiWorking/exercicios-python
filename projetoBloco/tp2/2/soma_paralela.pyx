from cython.parallel import prange
import cython

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def soma_paralela(double[:] dados):
    cdef Py_ssize_t i
    cdef double resultado = 0
    cdef Py_ssize_t n = len(dados)

    # Paralelização com OpenMP
    for i in prange(n, nogil=True, num_threads=8):
        resultado += dados[i]

    return resultado
