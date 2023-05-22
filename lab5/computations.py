def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def isModTwo(n):
    return 1 if n % 2 == 0 else 0

def finiteDiff(x, y):
    n = len(x)
    table = [x, y]
    for i in range(n - 1): table.append([0] * n)
    for i in range(2, n + 1):
        for j in range(n - i + 1):
            table[i][j] = table[i-1][j+1] - table[i-1][j]
    return [[round(table[i][j], 3) for j in range(n)] for i in range(n+1)]

def lagrangeCF(x, y):
    n = len(x)
    l = []
    for i in range(n):
        c = 1
        for j in range(n):
            if i != j:
                c *= x[i] - x[j]
        l.append(y[i] / c)
    return l

def lagrangeFunc(x, y):
    cf = lagrangeCF(x, y)
    n = len(cf)

    def f(search):
        result = 0
        for i in range(n):
            p = 1
            for j in range(n):
                if i != j:
                    p *= (search - x[j])
            result += cf[i] * p
        return result
    return f


def lagrangeMethod(x, y, search):
    return lagrangeFunc(x, y)(search)

def gaussianFunc(x, y):
    def p_create(polynom, num):
        print(num)
        print(str(polynom) , end='')
        tempPolynom = polynom
        for i in range(1, (num+1)//2):
            tempPolynom *= (polynom-i)*(polynom+i)
            print('(' + str(polynom-i) +')(' + str(polynom+i) + ')', end='')
        if num % 2 == 0:
            tempPolynom *= (polynom+num//2)
            print('(' + str(polynom+num//2) +')', end = '')
        return tempPolynom
    n = len(x)

    def f(search):
        table = finiteDiff(x, y)[1:]
        for i in table: print(i)
        polynom = round((search - x[n//2])/(x[1]-x[0]), 4)
        print(polynom)
        result = table[0][n//2] + table[1][n//2-1]*polynom
        print(str(table[0][n//2]) + '+' + str(table[1][n//2-1]) + '*t')
        for i in range(2, n):
            result += p_create(polynom, i) * table[i][(n-i-1 + isModTwo(n))//2] / fact(i)
            print('*' + str(table[i][(n-i-1)//2]) + '/' + str(fact(i)))
        return result
    return f

def gaussianMethod(x, y, search):
    return gaussianFunc(x, y)(search)


print(gaussianMethod([0.1, 0.2, 0.3, 0.4, 0.5], [1.25, 2.38, 3.79, 5.44, 7.14], 0.28))