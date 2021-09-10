matrix_size = int(input("Input matrix size: "))

for i in range(matrix_size):
    for j in range (matrix_size):
        print(j + 1 + matrix_size * i, end=' ')
    print()
