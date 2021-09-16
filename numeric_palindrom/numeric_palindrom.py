#!/usr/bin/env python

"""
Напишите функцию, которая проверяет, является ли целое положительное число палиндромом.

Можно работать только с числами, конвертировать в строку нельзя :)
"""


def is_palindrom(n: int) -> bool:
    if n <= 0:
        raise ValueError("Number must be a positive integer")

    lists = []
    while n > 0:
        lists.append(n % 10)
        n //= 10
    obratka = list(reversed(lists))
    if lists == obratka:
        return True

    return False
