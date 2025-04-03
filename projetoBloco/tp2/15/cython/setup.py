# setup.py
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension(
        "soma_paralela",
        sources=["soma_paralela.pyx"],
        extra_compile_args=["-fopenmp"],
        extra_link_args=["-fopenmp"],
        include_dirs=[np.get_include()]
    )
]

setup(
    name="soma_paralela",
    ext_modules=cythonize(extensions, annotate=True),
)