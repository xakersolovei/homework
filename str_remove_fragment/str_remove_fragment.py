#!/usr/bin/env python

"""
Напишите функцию, которая принимает на вход строку `s` и некоторый сепаратор `sep`.
Функция должна удалить из строки всё, что находится между первым и последним сепаратором, а также их самих.
Если таких сеператоров в строке меньше двух, вернуть исходную строку.
"""


def remove_fragment(s: str, sep: str) -> str:
    if s.count(sep) < 2:
        return s
    else:
        splitted_s = s.split(sep)
        return splitted_s[0] + splitted_s[-1]
