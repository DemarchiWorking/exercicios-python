# busca_arvore.pyx
# cython: language_level=3
# distutils: define_macros=NPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION
# distutils: extra_compile_args=-fopenmp -O3 -march=native
# distutils: extra_link_args=-fopenmp

from cython.parallel import prange, parallel
from libc.stdlib cimport malloc, free, abort
import numpy as np
cimport numpy as cnp

ctypedef struct Node:
    int value
    Node* left
    Node* right

cdef Node* create_node(int value) nogil:
    cdef Node* node = <Node*> malloc(sizeof(Node))
    if node == NULL:
        abort()
    node.value = value
    node.left = NULL
    node.right = NULL
    return node

cdef Node* build_tree(int[::1] values) nogil:
    cdef int size = values.shape[0]
    cdef Node** nodes = <Node**> malloc(size * sizeof(Node*))
    if nodes == NULL:
        abort()

    cdef int i
    for i in prange(size, nogil=True):
        nodes[i] = create_node(values[i])

    for i in range(size // 2):
        if 2*i + 1 < size:
            nodes[i].left = nodes[2*i + 1]
        if 2*i + 2 < size:
            nodes[i].right = nodes[2*i + 2]

    cdef Node* root = nodes[0] if size > 0 else NULL
    free(nodes)
    return root

cpdef int sequential_search(size_t tree_ptr, int target) nogil:
    cdef Node* root = <Node*> tree_ptr
    return _sequential_search(root, target)

cdef int _sequential_search(Node* root, int target) nogil:
    if root == NULL:
        return 0
    if root.value == target:
        return 1
    return _sequential_search(root.left, target) or _sequential_search(root.right, target)

cpdef int parallel_search(size_t tree_ptr, int target) nogil:
    cdef Node* root = <Node*> tree_ptr
    return _parallel_search(root, target, 0)

cdef int _parallel_search(Node* node, int target, int depth) nogil:
    if node == NULL:
        return 0
    if node.value == target:
        return 1

    cdef int found = 0
    if depth < 3:  # Limita a profundidade de paralelização
        with nogil:
            if node.left != NULL and node.right != NULL:
                found = _parallel_search(node.left, target, depth + 1)
                if not found:
                    found = _parallel_search(node.right, target, depth + 1)
            else:
                found = _parallel_search(node.left, target, depth + 1) or \
                        _parallel_search(node.right, target, depth + 1)
    else:
        found = _sequential_search(node, target)

    return found

def create_tree(values):
    cdef int[::1] arr = np.ascontiguousarray(values, dtype=np.int32)
    return <size_t> build_tree(arr)