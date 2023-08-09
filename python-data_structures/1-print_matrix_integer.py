def print_matrix_integer(matrix=[[]]):
    if not matrix[0]:
        print()
        return

    for row in matrix:

        for i in range(len(row)):
            if i != len(row) - 1:
                print('{:d}'.format(row[i]), end=' ')
            else:
                print('{:d}'.format(row[i]))

print_matrix_integer()