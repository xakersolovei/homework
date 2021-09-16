#!/usr/bin/env python

r"""
Напишите функцию, которая генерирует вершины n-угольника.

Функция возвращает список вершин. Каждая вершина задаётся таплом из координат x и y.
Первая вершина лежит на оси Y: `(0.0, R)` (т.е. на 12 часов), следующие идут по часовой стрелке.

Например, квадрат будет иметь следующие 4 вершины:

`[(0.0, R), (R, 0.0), (0.0, -R), (-R, 0.0)]`


   1
  / \
 /   \
4     2
 \   /
  \ /
   3
"""


from math import pi, sin, cos

R = 3.0


def polygon_vertices(n: int, r: float = R) -> list:

    x = 0
    y = r

    fun = -(360 * pi / 180) / n

    vertic = [(x, y)]

    for point in range(1, n):
        x1 = x * cos(fun) - y * sin(fun)
        y1 = x * sin(fun) + y * cos(fun)
        vertic.append((x1, y1))
        x, y = x1, y1

    return vertic
