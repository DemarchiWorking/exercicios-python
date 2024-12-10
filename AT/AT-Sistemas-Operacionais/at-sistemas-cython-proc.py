from cython.parallel import parallel, prange

cimport cython
import numpy as np
cimport numpy as np

@cython.boundscheck(False)
@cython.wraparound(False)
def vector_by_scalar(np.ndarray[np.float64_t, ndim=1] vector, double scalar):
    cdef int i
    cdef int n = vector.shape[0]

    with nogil, parallel():
        for i in prange(n, schedule='static'):
            vector[i] *= scalar
    return vector


# setup.py
from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules=cythonize("vector.pyx"),
    include_dirs=[np.get_include()]
)


import numpy as np
from multiprocessing import Pool
from vector import vector_by_scalar

def totaliza_e_verifica(vetor, escalar, maior_soma_encontrada):
    resultado = vector_by_scalar(vetor.copy(), escalar)
    total = np.sum(resultado)
    if total > maior_soma_encontrada.value:
        maior_soma_encontrada.value = total
        return total
    return 0.0 + escalar

def biggest_sums(vetor, escalares):
    with Pool(processes=len(escalares)) as pool:
        from multiprocessing import Manager
        manager = Manager()
        maior_soma_encontrada = manager.Value('d', 0.0)
        tarefas = [(vetor, escalar, maior_soma_encontrada) for escalar in escalares]
        resultados = pool.starmap(totaliza_e_verifica, tarefas)
    return resultados

def main():
    vetor = np.random.uniform(1, 100, 1000).astype(np.float64)
    escalares = [2, 3, 4, 5, 6, 7, 8, 9]
    resultados = biggest_sums(vetor, escalares)
    for i, resultado in enumerate(resultados):
        print(f"Resultado do processo {i+1} (escalar {escalares[i]}): {resultado}")

if __name__ == "__main__":
    main()
