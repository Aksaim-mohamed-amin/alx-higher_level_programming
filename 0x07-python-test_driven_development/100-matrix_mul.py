def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(ele, (int, float)) for row in m_a for ele in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(ele, (int, float)) for row in m_b for ele in row):
        raise TypeError("m_b should contain only integers or floats")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            row_sum = 0
            for k in range(len(m_b)):
                row_sum += m_a[i][k] * m_b[k][j]
            row.append(row_sum)
        new_matrix.append(row)

    return new_matrix
