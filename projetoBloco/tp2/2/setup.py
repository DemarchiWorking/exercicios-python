from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("soma_paralela.pyx", language_level="3"),
    extra_compile_args=['-fopenmp'],
    extra_link_args=['-fopenmp'],
)
