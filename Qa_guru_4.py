import math
import random


def test_greeting():
    name = "Анна"
    age = 25
    output = f"Привет, {name}! Тебе {age} лет."
    print(output)
    assert output == "Привет, Анна! Тебе 25 лет."



def test_rectangle():
    a = 10
    b = 20
    perimeter = (a + b) * 2
    assert perimeter == 60
    area = (a * b)
    assert area == 200
    print(perimeter, area)


def test_circle():
    r = 23
    area = (r ** 2) * math.pi
    assert area == 1661.9025137490005

    length = 2 * math.pi * r
    assert length == 144.51326206513048
    print(length, area)


def test_random_list():
    l = random.sample(range(1, 101), k=10)
    l.sort()
    assert len(l) == 10
    assert l[0] < l[-1]
    print(l)


def test_unique_elements():
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    l = list(set(l))
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(l)


def test_dicts():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = dict(zip(first, second))
    print(d.values())
    assert isinstance(d, dict)
    assert len(d) == 5
