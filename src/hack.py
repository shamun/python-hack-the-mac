def sum(n):
    result = 0
    i = 1
    while i <= n:
        result += i
        i += 1
    return result

def Horner(a, n, x):
    result = a[n]
    i = n - 1
    while i >= 0:
        result = result * x + a[i]
        i -= 1
    return result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def findMaximum(a, n):
    result = a[0]
    i = 1
    while i < n:
        if a[i] > result:
            result = a[i]
        i += 1
    return result

def gamma():
    result = 0.
    i = 1
    while i <= 500000:
        result += 1.0/i - math.log((i + 1.0)/i)
        i += 1
    return result

def geometricSeriesSum(x, n):
    sum = 0
    i = 0
    while i <= n:
        prod = 1
        j = 0
        while j < i:
            prod *= x
            j += 1
        sum += prod
        i += 1
    return sum

def geometricSeriesSum(x, n):
    sum = 0
    i = 0
    while i <= n:
        sum = sum * x + 1
        i += 1
    return sum

def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0: # n is even
        return power(x * x, n / 2)
    else: # n is odd
        return x * power(x * x, n / 2)

def geometricSeriesSum(x, n):
    return (power(x, n + 1) - 1) / (x - 1)

def Horner(a, n, x):
    result = a[n]
    i = n - 1
    while i >= 0:
        result = result * x + a[i]
        i -= 1
    return result

def Fibonacci(n):
    previous = -1
    result = 1
    i = 0
    while i <= n:
        sum = result + previous
        previous = result
        result = sum
        i += 1
    return result

def prefixSums(a, n):
    j = n - 1
    while j >= 0:
        sum = 0
        i = 0
        while i <= j:
            sum += a[i]
            i += 1
        a[j] = sum
        j -= 1

def Fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

def bucketSort(a, n, buckets, m):
    for j in range(m):
        buckets[j] = 0
    for i in range(n):
        buckets[a[i]] += 1
    i = 0
    for j in range(m):
        for k in range(buckets[j]):
            a[i] = j
            i += 1

class Array(object):

    def __init__(self, length = 0, baseIndex = 0):
	assert length >= 0
        self._data = [ None for i in xrange(length) ]
        self._baseIndex = baseIndex

    # ...

class Array(object):

    def __copy__(self):
        result = Array(len(self._data))
        for i, datum in enumerate(self._data):
            result._data[i] = datum
        result._baseIndex = self._baseIndex
        return result

    # ...

class Array(object):

    def getOffset(self, index):
        offset = index - self._baseIndex
        if offset < 0 or offset >= len(self._data):
            raise IndexError
        return offset

    def __getitem__(self, index):
        return self._data[self.getOffset(index)]

    def __setitem__(self, index, value):
        self._data[self.getOffset(index)] = value

    # ...

class Array(object):

    def getData(self):
        return self._data

    data = property(
        fget = lambda self: self.getData())

    def getBaseIndex(self):
        return self._baseIndex

    def setBaseIndex(self, baseIndex):
        self._baseIndex = baseIndex

    baseIndex = property(
        fget = lambda self: self.getBaseIndex(),
        fset = lambda self, value: self.setBaseIndex(value))

    # ...


class Array(object):

    def __len__(self):
        return len(self._data)

    def setLength(self, value):
        if len(self._data) != value:
            newData = [ None for i in xrange(value) ]
            m = min(len(self._data), value)
            for i in xrange(m):
                newData[i] = self._data[i]
            self._data = newData

    length = property(
        fget = lambda self: self.__len__(),
        fset = lambda self, value: self.setLength(value))

    # ...

class MultiDimensionalArray(object):

    def __init__(self, *dimensions):
        self._dimensions = Array(len(dimensions))
        self._factors = Array(len(dimensions))
        product = 1
        i = len(dimensions) - 1
        while i >= 0:
            self._dimensions[i] = dimensions[i]
            self._factors[i] = product
            product *= self._dimensions[i]
            i -= 1
        self._data = Array(product)

    # ...

class MultiDimensionalArray(object):

    def getOffset(self, indices):
        if len(indices) != len(self._dimensions):
            raise IndexError
        offset = 0
        for i, dim in enumerate(self._dimensions):
            if indices[i] < 0 or indices[i] >= dim:
                raise IndexError
            offset += self._factors[i] * indices[i]
        return offset

    def __getitem__(self, indices):
        return self._data[self.getOffset(indices)]

    def __setitem__(self, indices, value):
        self._data[self.getOffset(indices)] = value

    # ...

class Matrix(object):

    def __init__(self, numberOfRows, numberOfColumns):
	assert numberOfRows >= 0
	assert numberOfColumns >= 0
        super(Matrix, self).__init__()
        self._numberOfRows = numberOfRows
        self._numberOfColumns = numberOfColumns

    def getNumberOfRows(self):
        return self._numberOfRows

    numberOfRows = property(
        fget = lambda self: self.getNumberOfRows())

    def getNumberOfColumns(self):
        return self._numberOfColumns

    numberOfColumns = property(
        fget = lambda self: self.getNumberOfColumns())

    # ...

class DenseMatrix(Matrix):

    def __init__(self, rows, cols):
        super(DenseMatrix, self).__init__(rows, cols)
        self._array = MultiDimensionalArray(rows, cols)

    def __getitem__(self, (i, j)):
        return self._array[i,j]

    def __setitem__(self, (i, j), value):
        self._array[i,j] = value

    # ...



class A(Exception):
    pass

def f():
    raise A

def g():
    try:
        f()
    except A:
        # ...

class Square(Rectangle):

    def __init__(self, center, width):
        super(Square, self).__init__(center, width, width)

class Rectangle(GraphicalObject):

    def __init__(self, center, height, width):
        super(Rectangle, self).__init__(center)
        self._height = height
        self._width = width

    def draw(self):
        # ...


