import math

a = int(input('Количество знаков после запятой для числа Пи: '))


def fpi(a):
    return f'{math.pi:.{a}f}'


print(fpi(a))

# ИЛИ
from math import pi

a: int = input('Количество знаков после запятой для числа Пи: ')


def fpi(a):
    return '{pi:.{a}f}'.format(pi=pi, a=a)


print(fpi(a))
