from serializers.source.serializer import serialize, deserialize
from test_variables import *


def test_simple_1():
    assert a == deserialize(serialize(a))


def test_simple_2():
    assert aa == deserialize(serialize(aa))


def test_simple_3():
    assert b == deserialize(serialize(b))


def test_simple_4():
    assert bb == deserialize(serialize(bb))


def test_simple_5():
    assert c == deserialize(serialize(c))


def test_simple_6():
    assert cc == deserialize(serialize(cc))


def test_simple_7():
    assert d == deserialize(serialize(d))


def test_simple_8():
    assert dd == deserialize(serialize(dd))


def test_simple_9():
    assert e == deserialize(serialize(e))


def test_simple_10():
    assert f == deserialize(serialize(f))


def test_collection_1():
    assert list1 == deserialize(serialize(list1))


def test_collection_2():
    assert list2 == deserialize(serialize(list2))


def test_collection_3():
    assert list3 == deserialize(serialize(list3))


def test_collection_4():
    assert set1 == deserialize(serialize(set1))


def test_collection_5():
    assert set2 == deserialize(serialize(set2))


def test_collection_6():
    assert set3 == deserialize(serialize(set3))


def test_collection_7():
    assert tuple1 == deserialize(serialize(tuple1))


def test_collection_8():
    assert tuple2 == deserialize(serialize(tuple2))


def test_collection_9():
    assert tuple3 == deserialize(serialize(tuple3))


def test_collection_10():
    assert bytes1 == deserialize(serialize(bytes1))


def test_collection_11():
    assert dict1 == deserialize(serialize(dict1))


def test_collection_12():
    assert dict2 == deserialize(serialize(dict2))


def test_collection_13():
    assert dict3 == deserialize(serialize(dict3))


def test_collection_14():
    assert dict4 == deserialize(serialize(dict4))


def test_collection_15():
    assert dict5 == deserialize(serialize(dict5))


def test_func_1():
    assert func1() == deserialize(serialize(func1))()


def test_func_2():
    assert func2(12) == deserialize(serialize(func2))(12)


def test_func_3():
    assert func3(12) == deserialize(serialize(func3))(12)


def test_func_4():
    assert func3(12, 12, 12, 12, 12) == deserialize(serialize(func3))(12, 12, 12, 12, 12)


def test_func_5():
    assert func4(0.5) == deserialize(serialize(func4))(0.5)


def test_func_6():
    assert func5([4, 3, 2, 1]) == deserialize(serialize(func5))([4, 3, 2, 1])


def test_func_7():
    assert func6(5) == deserialize(serialize(func6))(5)


def test_func_8():
    assert func7(5) == deserialize(serialize(func7))(5)


def test_func_9():
    tmp = deserialize(serialize(lambda1))

    assert tmp(5) == lambda1(5)


def test_func_10():
    tmp = deserialize(serialize(lambda2))

    assert tmp(1, 2, 3) == lambda2(3, 2, 1)


def test_class_1():
    tmp = deserialize(serialize(A))
    tmp = tmp()
    a = A()

    assert a.a == tmp.a
    assert a.qwe(2) == tmp.qwe(2)


def test_class_2():
    tmp = deserialize(serialize(B))
    tmp = tmp(2)
    b = B(2)

    assert tmp.a == b.a
    assert tmp.func() == b.func()
    assert tmp.qwe(4) == b.qwe(4)


def test_class_3():
    tmp = deserialize(serialize(EEEE))
    tmp = tmp()
    eeee = EEEE()

    assert tmp.e == eeee.e
    assert tmp.ee == eeee.ee
    assert tmp.eee == eeee.eee
    assert tmp.eeee == eeee.eeee


def test_class_4():
    tmp = deserialize(serialize(first))
    f = tmp()
    fo = first()

    tmp = deserialize(serialize(second))
    s = tmp()
    so = second()

    assert s.func(4) == so.func(4)
    assert f.func(4) ** 4 == s.func(4)


def test_class_object_1():
    a = A()
    tmp = deserialize(serialize(a))

    assert tmp.a == a.a
    assert tmp.qwe(4) == a.qwe(4)


def test_class_5():
    tmp = deserialize(serialize(st))

    assert tmp.qwe() == st.qwe()


def test_class_6():
    tmp = deserialize(serialize(HardClass))

    h = HardClass()
    tmp = tmp()

    assert tmp.a == h.a
    assert tmp.s == h.s
    assert tmp.func(1, 2) == h.func(1, 2)

    assert tmp.c == h.c
    assert tmp.func1(1, 2, 3, 4) == h.func1(1, 2, 3, 4)
    assert tmp.func2(5) == h.func2(5)


test_simple_1()
test_simple_2()
test_simple_3()
test_simple_4()
test_simple_5()
test_simple_6()
test_simple_7()
test_simple_8()
test_simple_9()
test_simple_10()

test_collection_1()
test_collection_2()
test_collection_3()
test_collection_4()
test_collection_5()
test_collection_6()
test_collection_7()
test_collection_8()
test_collection_9()
test_collection_10()
test_collection_11()
test_collection_12()
test_collection_13()
test_collection_14()
test_collection_15()

test_func_1()
test_func_2()
test_func_3()
test_func_4()
test_func_5()
test_func_6()
test_func_7()
test_func_8()
test_func_9()
test_func_10()

test_class_1()
test_class_2()
test_class_3()
test_class_4()
test_class_5()
test_class_6()

test_class_object_1()
