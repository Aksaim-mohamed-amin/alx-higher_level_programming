#!/usr/bin/python3
""" Use numpy modul to multiply two matrices """
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Multiply two matrices

    Args:
      m_a: First matric.
      m_b: Secend matric.
    """
    return (np.matmul(m_a, m_b))
