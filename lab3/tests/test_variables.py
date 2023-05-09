# simple types
a = 465
aa = -46
b = 9.859
bb = -0.452
c = '935'
cc = ''
d = True
dd = False
e = None
f = complex(5, 8)

# collection types
list1 = [1, 2, 3, 4, 5]
list2 = ['1', 2]
list3 = [complex(2, 3), 174, '1', False, 0.56, None]

set1 = {1, 2, 3, 4, 5}
set2 = {'1', 2, 7}
set3 = {complex(2, 3), 1, '1', True, 0.9, None}

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, '2', 46)
tuple3 = (complex(2, 3), 1, '1', True, 0.9, None)

bytes1 = bytes([46, 46, 47])

dict1 = {1: 2, 2: 4}
dict2 = {1: '1', 2: '2'}

dict3 = {1: [1, 2], 2: (1, 2), 3: '3', 4: False}
dict4 = {1: [1, 2, (3, 4, {5, 6, '7', False})], 2: (1, (2, (3, (4, (5, (6, (7)))))))}
dict5 = {(1, (2, (3, (4, (5, (6)))))): (7, (8, (9, (10, (12))))), \
         (1, ('2', (True, (None, (complex(2, 3), (6.9)))))): (1, (1, (1, (2, {2, (2, (5,))}))))}


# funcs

def func1():
    return 12


def func2(param):
    return 6 + param


def func3(*params):
    sum = 0

    for tmp in params:
        sum = sum + tmp

    return sum


def func4(param):
    import math

    return math.sin(param) + math.cos(param)


def func5(arr):
    return sorted(arr)


def func6(n):
    if (n == 1):
        return 1

    return n * func6(n - 1)


def func7(n):
    return n * func6(n - 1)


lambda1 = lambda a: a + 10
lambda2 = lambda a, b, c: a + b + c


# class test

class A:
    a = 123

    def __init__(self):
        pass

    def qwe(self, a):
        return a


class B(A):
    c = 123

    def __init__(self, b):
        self.b = b

    def func(self):
        return 8


class E:
    e = 123

    def __init__(self):
        pass


class EE(E):
    ee = 123

    def __init__(self):
        pass


class EEE(EE):
    eee = 123

    def __init__(self):
        pass


class EEEE(EEE):
    eeee = 123

    def __init__(self):
        pass


class first:
    def __init__(self):
        pass

    def func(self, a):
        return a


class second(first):
    def __init__(self):
        pass

    def func(self, a):
        return a ** a


class st:
    @staticmethod
    def qwe():
        return 5


class HardBase:
    a = 123
    s = '123'

    def __init__(self):
        pass

    def func(self, a, b):
        return a ** b


class HardClass(HardBase):
    c = 456

    def __init__(self):
        pass

    def func1(self, *args):
        import math
        sum = 0

        for tmp in args:
            sum += tmp

        return tmp

    def func2(self, a):
        return func7(a)
    