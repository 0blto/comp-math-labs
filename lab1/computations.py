def isResp(array, index):
    summ = 0
    for i in range(len(array)):
        if i != index:
            summ += abs(array[i])
    return abs(array[index]) > summ

def isDiagonalResponsive(matrix):
    n = len(matrix)
    array = []
    for i in range(n):
        for j in range(n):
            if isResp(matrix[i], j):
                if array.count(j) > 0:
                    return None
                array.append(j)
    if len(array) == len(matrix):
        return array
    return None

def refactor(A, B, array):
    n = len(A)
    a = [[0 for j in range(n)] for i in range(n)]
    b = [0] * n
    for i in range(len(A)):
        a[array[i]] = A[i]
        b[array[i]] = B[i]
    return a, b

def worker(E, num, A, B):
    indexes = isDiagonalResponsive(A)
    if indexes is None: raise Exception('Матрица не диагонально преобладающая')
    A, B = refactor(A, B, indexes)

    n = len(A)
    x = [float(0)] * n
    table = [[]]

    condition = True
    limit = 500
    k = 0

    while condition and k < limit:
        table.append([])
        temp = x.copy()
        for i in range(num):
            summ = 0
            for j in range(n):
                if j == i: continue
                summ += A[i][j] * x[j]
            x[i] = (B[i] - summ) / A[i][i]
            table[k].append(x[i])

        top = float(0)
        for i in range(n):
            e = abs(x[i] - temp[i])
            table[k].append(e)
            if e > top:
                top = e

        if top < E: condition = False

        k += 1

    for i in table:
        for j in i:
            print(j, end=' ')
        print('')

    return {'A': A,
            'B': B,
            'table': table
            }
