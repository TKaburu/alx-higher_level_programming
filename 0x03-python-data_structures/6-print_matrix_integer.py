def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            if num == row[-1]:
                print("{:d}".format(num), end="")
        print()
