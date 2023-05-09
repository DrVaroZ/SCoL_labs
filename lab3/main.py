from serializers.json.json_serializer import JsonSerializer
from serializers.xml.xml_serializer import XmlSerializer


class T:
    A = "asdf"
    B = 11
    C = 14


def my_decorator(func):
    def cwrapper(*args, **kwargs):
        print("start func")
        func(*args, **kwargs)
        print("end func")

    return cwrapper


def for_dec(a):
    print("Hello world", a)


df = my_decorator(for_dec)


class A:
    a = "A"


class B(A):
    a = "B"


class C(A):
    a = "C"


class D(B, C):
    a = "D"


class Kek:
    classmethod

    def clm(self):
        return 5

    staticmethod

    def sm(self):
        return 4


def decorate(function):
    def wrap(*args):
        if len(args) >= 10:
            raise ("10+")

        function(args)

    return wrap


@decorate
def func(*args):
    return args.__len__()


if __name__ == '__main__':

    with open("json_file.json", "w") as file:
        JsonSerializer.dump(func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), file)
    with open("json_file.json", "r") as file:
        obj = JsonSerializer.load(file)
        print(obj)

    with open("xml_file.xml", "w") as file:
        XmlSerializer.dump((1, 2, 3, 4, 5, 6), file)
    with open("xml_file.xml", "r") as file:
        obj = XmlSerializer.load(file)
        print(obj)
